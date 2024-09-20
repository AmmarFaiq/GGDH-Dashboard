import dash
from dash import html, dcc, dash_table
import pandas as pd
import plotly.graph_objects as go
import os

dash.register_page(__name__)

layout = html.Div([
    html.H1('About the Dashboard'),
    dcc.Markdown(
    """
    ELAN-H/GP (Huisartsen) is een uniek huisartsen-netwerk met (op dit moment) meer dan 140 
    deelnemende huisartsen en data van meer dan 800.000 patiënten in de ELAN-huisartsendata. 
    Via ELAN-H zijn inmiddels tientallen onderzoeken verricht en we hopen dat in de komende jaren voort 
    te kunnen zetten.
    """),
    html.H1('ELAN-DCC Team'),
    dcc.Markdown(
    """
    ELAN-H/GP (Huisartsen) is een uniek huisartsen-netwerk met (op dit moment) meer dan 140 
    deelnemende huisartsen en data van meer dan 800.000 patiënten in de ELAN-huisartsendata. 
    Via ELAN-H zijn inmiddels tientallen onderzoeken verricht en we hopen dat in de komende jaren voort 
    te kunnen zetten.
    """),
    html.H1('Supply and Demand Themes'),
    dcc.Markdown(
    """
    ELAN-H/GP (Huisartsen) is een uniek huisartsen-netwerk met (op dit moment) meer dan 140 
    deelnemende huisartsen en data van meer dan 800.000 patiënten in de ELAN-huisartsendata. 
    Via ELAN-H zijn inmiddels tientallen onderzoeken verricht en we hopen dat in de komende jaren voort 
    te kunnen zetten.
    """),
    html.H1('Hartfalen Themes'),
    dcc.Markdown(
    """
    ELAN-H/GP (Huisartsen) is een uniek huisartsen-netwerk met (op dit moment) meer dan 140 
    deelnemende huisartsen en data van meer dan 800.000 patiënten in de ELAN-huisartsendata. 
    Via ELAN-H zijn inmiddels tientallen onderzoeken verricht en we hopen dat in de komende jaren voort 
    te kunnen zetten.
    """),
#     html.P([html.A('GGDH-ELAN', href='https://gezondengelukkigdenhaag.nl/', target='_blank'),
#            ',',
#            html.A('Microdata CBS', href='https://www.cbs.nl/en-gb/our-services/customised-services-microdata/microdata-conducting-your-own-research', target='_blank')])
    ])