import dash
from dash import dcc, html, Input, Output, State, callback
import dash_daq as daq
import dash_bootstrap_components as dbc
import numpy as np
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots
from matplotlib.colors import LinearSegmentedColormap, to_hex
import geopandas as gpd
import requests
import json
import math

import os
import util.translate as tr
import util.bivariate_plot 


# style
colorscale = ["#402580", "#38309F", "#3C50BF", "#4980DF", "#56B7FF", "#6ADDFF", "#7FFCFF", "#95FFF5", "#ABFFE8", "#C2FFE3", "#DAFFE6"]
elan_cm = LinearSegmentedColormap.from_list("pretty_elan", colorscale, N=len(colorscale))
    
style = {"fontsize": 12,
         "color": "#808080",
         "slider": "#ADD8E6"}

def get_colors(min_thresh: float, resample: int) -> list:
    '''helper function to sample colours'''
    step = (1 - min_thresh)/resample
    return [to_hex(elan_cm(i)) for i in np.arange(0, 1.0-min_thresh, step)] 
# end style

# values_haaglanden=["'s-Gravenhage",
#         "Delft","Leidschendam-Voorburg",
#         "Midden-Delfland", 
#         "Pijnacker-Nootdorp","Rijswijk",
#         "Wassenaar","Westland","Zoetermeer"]

# values_roaz=["'s-Gravenhage", "Alphen aan den Rijn", "Bodegraven-Reeuwijk",
#         "Delft","Gouda","Hillegom", "Kaag en Braassem","Katwijk",
#         "Krimpenerwaard","Leiden","Leiderdorp", "Leidschendam-Voorburg",
#         "Lisse","Midden-Delfland","Nieuwkoop","Noordwijk","Oegstgeest",
#         "Pijnacker-Nootdorp","Rijswijk","Teylingen","Voorschoten", "Waddinxveen",
#         "Wassenaar","Westland","Zoetermeer","Zoeterwoude","Zuidplas"]

# values_all_regions = values_haaglanden + values_roaz

# # values_all_regions_gementee = [s + "Gemeente " for s in values_all_regions]
# # values_all_regions = [s + "Gemeente " for s in values_all_regions]

dash.register_page(__name__)

path = '../data/'
path = os.path.join(os.path.dirname(__file__), path).replace("\\","/").replace("pages" + "/../","")

geo_df= gpd.read_file(path + 'wijk_2023_v0.shp')

geo_df= geo_df.to_crs(epsg=4326)

geo_df.rename(columns ={'WK_CODE':'WKC'}, inplace = True)

# geofilepath = requests.get(path + 'wijkgeo_file.json')

# geo_df_fff = json.loads(geofilepath.content)

# geo_df = geo_df.query("GM_NAAM in @values_all_regions")

df_numeric = pd.read_csv(path + 'df_numeric_ver_3.csv', sep=',', encoding='latin-1')
df_count = pd.read_csv(path + 'df_count_ver_3.csv', sep=',',encoding= 'latin-1')
df = df_count.merge(df_numeric, on=['WKC','Wijknaam','GMN','YEAR'])

df_demand_CLUSTERED = pd.read_csv(path + 'df_demand_CLUSTERED_3.csv')
df_demand_CLUSTERED_proj = pd.read_csv(path + 'df_demand_CLUSTERED_proj_3.csv')
data_projected_clust_pred = pd.read_csv(path + 'data_projected_clust_pred_3.csv')

# change negative values to 0
cols = data_projected_clust_pred.select_dtypes(include=np.number).columns
data_projected_clust_pred[cols] = data_projected_clust_pred[cols].clip(lower=0)
data_projected_clust_pred['Total_Population'] = data_projected_clust_pred['Total_Population'].astype(int)

# change negative values to 0
cols = df_demand_CLUSTERED_proj.select_dtypes(include=np.number).columns
df_demand_CLUSTERED_proj[cols] = df_demand_CLUSTERED_proj[cols].clip(lower=0)
df_demand_CLUSTERED_proj['Total_Population'] = df_demand_CLUSTERED_proj['Total_Population'].astype(int)

df_demand_CLUSTERED_Year = pd.read_csv(path + 'df_demand_CLUSTERED_Year_3.csv')

df_supply_CLUSTERED = pd.read_csv(path + 'df_supply_CLUSTERED_3.csv')

# order df_demand_CLUSTERED_Year by YEAR
df_demand_CLUSTERED_Year = df_demand_CLUSTERED_Year.sort_values(by=['YEAR','Cluster_Reworked'])

df_demand_CLUSTERED_Year['Cluster_Reworked'] = df_demand_CLUSTERED_Year['Cluster_Reworked'].astype(str)

df_projected = pd.read_csv(path + 'data_projected_3.csv')

values_hadoks= ("'s-Gravenhage", "Leidschendam-Voorburg", "Rijswijk", "Wassenaar")

# values_values_hadoks_gementee = [s + "Gemeente " for s in values_hadoks]

#this way, we can always extend the number of special regions, without having to tamper with the rest of the code
#could even be read in from a file or sth to keep it from being hardcoded.
special_regions = {"Hadoks' area": values_hadoks}

layout = html.Div([
    html.H1('Supply vs Demand page' + str(path))])