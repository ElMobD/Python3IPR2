#######################################
#####      Tous les imports      ######
#######################################

import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
from data import getCsvByLink
import plotly.express as px

#Variable Globale
app = dash.Dash(__name__) 


#Layout principale du DashBoard
app.layout = html.Div(
    id='container',
    style={'width': '100%', 'height': '97.5vh', 'background-color': 'gray', 'display': 'flex', 'flex-direction': 'column', 'align-items': 'center'},
    children=[
        html.Div(
            id='statistique-container',
            style={'flex': '5', 'background-color': 'pink'},
            children=[
               html.Div([
                    dcc.Location(id='url', refresh=False),
                    html.Div(id='page-content', style={'backgroundColor': '#f4f4f4', 'padding': '20px'})
                ])
            ]
        ),
        html.Div(
            id='button-container',
            style={'flex':'1','width': '20%', 'display': 'flex', 'align-items': 'center', 'justify-content': 'space-between'},
            children=[
                dcc.Link(
                    html.Button(
                        'Histogramme',
                        id='button-histogramme'
                    ),
                    href='/page-1',
                ),
                dcc.Link(
                    html.Button(
                        'Map',
                        id='button-map'
                    ),
                    href='/page-2'
                )
            ]
        )
    ]
)


@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def display_page(pathname):
    if pathname is None or pathname == '/':
        return layout_page_1
    elif pathname == '/page-1':
        return layout_page_1
    elif pathname == '/page-2':
        return layout_page_2
    else:
        return '404 Page not found'    

# Layout de la page 1
layout_page_1 = html.Div([
    html.H1('Page 1'),
    html.P('Contenu de la page 1...')
])

# Layout de la page 2
layout_page_2 = html.Div([
    html.H1('Page 2'),
    html.P('Contenu de la page 2...')
])   
def createHistogramme():
    dataFrame = pd.read_csv("data/dynamicData.csv", sep = ',')
    result = dataFrame.loc[
        (dataFrame['State'] == 'United States') 
        & (dataFrame['Sex'] == 'All Sexes') 
        & (dataFrame['Group'] == 'By Total')]
    print(result)

def createMap():
    print("Création de la map")
    
def createCsvFile(apiURL):
    getCsvByLink.get_and_save_csv(apiURL, "data/dynamicData.csv") 
    
def launchApp():
    app.run_server(debug=True)

def main():
    createCsvFile("https://data.cdc.gov/api/views/9bhg-hcku/rows.csv?accessType=DOWNLOAD")
    createHistogramme()
    #launchApp()

if __name__ == "__main__":
    main()



#HISTOGRAME abcise => âge & ordonnée => nombre morts totale et nombre mort covid
#MAP 