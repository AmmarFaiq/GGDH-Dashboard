import dash
from dash import dcc, html, Input, Output, State
import util.translate as tr

external_stylesheets = [
    'https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100..900;1,100..900&family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap',
]
app = dash.Dash(__name__, use_pages= True, title="Gezond en Gelukkig Den Haag",
                external_stylesheets=external_stylesheets)

server = app.server
app._favicon = "favicon.svg"

navbar = html.Div(
    html.Div(
        [

            html.Div(html.A(html.Img(src= app.get_asset_url('hc-dh-logo.svg')), href= 'https://healthcampusdenhaag.nl/nl/'), id="headerlogo"),
            html.Div([html.H1("ELAN Neighbourhood Dashboard"), html.P('Last updated January 2024', id="last_update")], id= 'headersub'),
            html.Div(html.Button('Menu', id="menu_button"), id="icon"),
            html.Div(
                    [dcc.Link('Neighbourhood', href= '/'),
                    dcc.Link('Supply and Demand', href='/supplydemand'),
                    dcc.Link("Diabetes", href="/diabetes"),
                    dcc.Link("Palliative Care", href="/palliative"),
                    dcc.Link("Pedriatric Care", href="/palliative"),
                    ], id= "navmenu", className="nav_closed"),
            html.Div(html.Img(src=app.get_asset_url('flag-EN.svg'), alt=tr.Language.EN.value,  id='select_language'), id='lang_select_parent')
        ], id ="headercontent"),
    id= 'header'
)


# Health Campus Den Haag
# Turfmarkt 99, 3de etage
# 2511 DP Den Haag
footer = html.Div(html.Div([
                html.Div([
                    html.P([
                        html.H1('Health Campus Den Haag'), html.Br(),'Turfmarkt 99', html.Br(), '3rd floor', html.Br(), '2511 DP, Den Haag'], id="footerleft")
                ], className= 'footerelement'), 
                html.Div([
                    html.Ul([html.Li(dcc.Link('About Us', href= '/about')), html.Li(dcc.Link('Variables Explanation', href= '/changelog')), 
                             html.Li(dcc.Link('Data Availability', href= '/changelog')), html.Li(dcc.Link('Changelog', href= '/changelog'))])
                ], className= 'footerelement'),
                html.Div([
                    html.H1('Partners'),
                    html.A([html.Img(src=app.get_asset_url('logo lumc_PMS_NL.svg'))], href='https://www.lumc.nl/en/'),
                    html.A([html.Img(src=app.get_asset_url('UL - Algemeen - RGB-Kleur.svg'))], href='https://www.universiteitleiden.nl/en'),
                    html.A([html.Img(src=app.get_asset_url('hhs_nl_groen_fc-2018.svg'))], href='https://www.dehaagsehogeschool.nl/'),                                                   
                    html.A([html.Img(src=app.get_asset_url('HMC_logo.svg'))], href='https://www.haaglandenmc.nl/'),  
                    html.A([html.Img(src=app.get_asset_url('Haga_logo.svg'))], href='https://www.hagaziekenhuis.nl/home/'),
                    html.A([html.Img(src=app.get_asset_url('hadoks_logo.svg'))], href='https://www.hadoks.nl/'),
                    html.A([html.Img(src=app.get_asset_url('PAR_Groep+po_line_01_CMYK_FC.svg'))], href='https://www.parnassia.nl/'),
                    html.A([html.Img(src=app.get_asset_url('logo1-rgb.svg'))], href='https://reinierdegraaf.nl/'),
                    html.A([html.Img(src=app.get_asset_url('Compact_Logo_gemeente_Den_Haag.svg'))], href='https://www.denhaag.nl/nl.htm'),
                    ], id = 'partners', className = 'footerelement'),
            ], id = 'footercontent'), id="footer")


app.layout = html.Div([dcc.Store(id='session', storage_type='session'), navbar,    
    html.Div(html.Div(html.Div(dash.page_container, id='main', className= 'toggle'))),
    footer
])


#------------------------------------------------------ Callbacks ------------------------------------------------------

# navigation
@app.callback(
    Output("navmenu", "className"),
    [Input("menu_button", "n_clicks")],
    [State("navmenu", "className")],
    prevent_initial_call=True
)

def toggle_navbar_collapse(n, classname):
    if classname == "nav_open":
        return "nav_closed"
    return "nav_open"

# language
@app.callback(
    Output('select_language', 'alt'),
    Output('select_language', 'src'),
    Output('session', 'data'),
    Input('select_language', 'alt'),
    Input('lang_select_parent', 'n_clicks'),
    prevent_initial_call=False
)
def update_language(value, clicks):

    if value == tr.Language.EN.value:
        value = tr.Language.NL.value
        flag = app.get_asset_url('flag-EN.svg')
    else:
        value = tr.Language.EN.value
        flag = app.get_asset_url('flag-NL.svg')
            
    tr.change_language(value)
    return value, flag, (value)

# localisation (chained)
@app.callback(
    Output('last_update', 'children'),
    Output('navmenu', 'children'),
    Output('footerleft', 'children'),
    Input('session', 'data')
)
def localise(language):
    last_update = (tr.translate("last update") + tr.translate_date(1))
    nav =  [dcc.Link(tr.translate('Neighbourhood'), href= '/'),
            dcc.Link(tr.translate('Supply and Demand'), href='/supplydemand'),
            dcc.Link(tr.translate("Diabetes"), href="/diabetes"),
            dcc.Link(tr.translate("Palliative care"), href="/palliative"),
            dcc.Link(tr.translate("Pedriatric care"), href="/pedriatric")]
    footer = html.P([html.H1('Health Campus Den Haag'),'Turfmarkt 99', html.Br(),
                     tr.translate('3rd floor'), html.Br(), '2511 DP, Den Haag'])
    return last_update, nav, footer


if __name__ == '__main__':
    app.run_server(debug=True,  dev_tools_hot_reload=False)



