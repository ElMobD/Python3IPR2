#######################################
#####      Tous les imports      ######
#######################################

import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
from data import getCsvByLink
from function import function
import plotly.express as px
import plotly.graph_objects as go
import json

#Variable Globale
app = dash.Dash(__name__) 
app.config.suppress_callback_exceptions = True
CsvDataFrame = pd.read_csv("data/dynamicData.csv", sep = ',')
all_states = function.getAllState(CsvDataFrame)


#Layout principale du DashBoard
app.layout = html.Div(
    id='container',
    style={'width': '100%', 'height': '97.5vh', 'background-color': 'gray', 'display': 'flex', 'flex-direction': 'column', 'align-items': 'center'},
    children=[
        html.Div(
            id='statistique-container',
            style={'flex': '5', 'background-color': 'pink', 'width': '100%'},
            children=[
                html.Div(
                    style={'width':'100%', 'height':'100%', 'display': 'grid', 'place-items':'center'},
                    children=[
                        dcc.Location(id='url', refresh=False),
                        html.Div(id='page-content', style={'backgroundColor': '#f4f4f4', 'padding': '20px', 'width':'90%', 'height': '100%', 'display': 'grid', 'place-items':'center'})
                    ]
                )
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

def createHistogramme(filter):
    newDataFrame = function.createHistoDf(CsvDataFrame, filter)
    fig = px.bar(newDataFrame, x='Age Group', y=['Total Deaths', 'COVID-19 Deaths'], barmode='group', title="Nombre de morts totales / Nombre de morts Covid-19 en ("+filter+")")
    return fig

def createMap():
    df = function.createMapDf(CsvDataFrame)
    print(df)
    fig = go.Figure(data=go.Choropleth(
            locations=df['code'],
            z=df['Total Deaths'].astype(float),
            locationmode='USA-states',
            colorscale='Reds',
            autocolorscale=False,
            marker_line_color='white', # line markers between states
            colorbar_title="Nombre de morts"
        ))  
    fig.update_layout(
        title_text = 'Nombre de morts total par état de 2020 à septembre 2023',
        geo_scope='usa', # limite map scope to USA
    )   
    return fig


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

@app.callback(Output('histogram', 'figure'),[Input('filter', 'value')])
def update_histogram(selected_state):
    return createHistogramme(selected_state)


# Layout de la page 1
layout_page_1 = html.Div(
    style={'width': '100%', 'height':'100%'},
    children=[
        dcc.Graph(
            id='histogram',
            style={'height':'70vh'},
            figure = createHistogramme('United States')
        ),
        dcc.Dropdown(
            id='filter',
            options=[{'label': state, 'value': state} for state in all_states],
            value='United States',  
            multi=False
        )
    ]
)

# Layout de la page 2
layout_page_2 = html.Div(
    children=[
        dcc.Graph(figure=createMap())
    ]
)   


def createCsvFile(apiURL):
    getCsvByLink.get_and_save_csv(apiURL, "data/dynamicData.csv") 
    
def launchApp():
    app.run_server(debug=True)

def main():
    createCsvFile("https://data.cdc.gov/api/views/9bhg-hcku/rows.csv?accessType=DOWNLOAD")
    launchApp()

if __name__ == "__main__":
    main()


