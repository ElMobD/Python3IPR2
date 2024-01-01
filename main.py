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


#Variable Globale
app = dash.Dash(__name__) 
app.config.suppress_callback_exceptions = True
CsvDataFrame = pd.read_csv("data/dynamicData.csv", sep = ',')
all_states = function.getAllState(CsvDataFrame)


#Layout principale du DashBoard
app.layout = html.Div(
    id='container',
    style={'width': '100%', 'height': '97.5vh','display': 'flex', 'flex-direction': 'column', 'align-items': 'center'},
    children=[
        html.Div(
            id='statistique-container',
            style={'flex': '5', 'width': '100%'},
            children=[
                html.Div(
                    style={'width':'100%', 'height':'100%', 'display': 'grid', 'place-items':'center'},
                    children=[
                        dcc.Location(id='url', refresh=False),
                        html.Div(id='page-content', style={'padding': '20px', 'width':'90%', 'height': '100%', 'display': 'grid', 'place-items':'center'})
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
    fig = px.bar(newDataFrame, x='Age Group', y=['Total Deaths', 'COVID-19 Deaths'], barmode='group', title="Nombre de morts totals / Nombre de morts Covid-19 en ("+filter+")")
    return fig

def createMap(number):
    filter = function.getSliderValueName(number)
    df = function.createMapDf(CsvDataFrame, filter)
    fig = go.Figure(data=go.Choropleth(
            locations=df['code'],
            z=df[filter].astype(float),
            locationmode='USA-states',
            colorscale='Reds',
            autocolorscale=False,
            marker_line_color='white', 
            colorbar_title="Nombre de morts"
        ))  
    fig.update_layout(
        title_text = 'Nombre de morts ('+filter+') par état de 2020 à septembre 2023',
        geo_scope='usa', 
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

@app.callback(Output('map-graph', 'figure'),[Input('my-slider', 'value')])
def update_map(number):
    return createMap(number)

# Layout de la page 1
layout_page_1 = html.Div(
    style={'width': '100%', 'height':'100%', 'position': 'relative'},
    children=[
        dcc.Graph(
            id='histogram',
            style={'height':'70vh'},
            figure = createHistogramme('United States')
        ),
        dcc.Dropdown(
            style={'width':'30%', 'position': 'absolute', 'left': '50%', 'bottom': '0','transform': 'translate(-58.5%, -180%)'},
            id='filter',
            options=[{'label': state, 'value': state} for state in all_states],
            value='United States',  
            multi=False
        )
    ]
)

# Layout de la page 2
layout_page_2 = html.Div(
    style={'width': '100%', 'height': '100%', 'display': 'grid', 'gridTemplateColumns': '1fr', 'gridTemplateRows': '2fr 1fr'},
    children=[
        html.Div(
            dcc.Graph(
                id='map-graph',
            ),
            style={'grid-column': '1', 'grid-row': '1', 'width': '100%', 'height': '100%'}
        ),
        html.Div(
            dcc.Slider(
                id='my-slider',
                min=1,
                max=6,
                value=1,
                step=1,
                updatemode="drag",
                marks={
                    1: 'Total Deaths',
                    2: 'COVID-19 Deaths',
                    3: 'Pneumonia Deaths',
                    4: 'Pneumonia and COVID-19 Deaths',
                    5: 'Influenza Deaths',
                    6: 'Pneumonia, Influenza, or COVID-19 Deaths'
                },
            ),
            style={'grid-column': '1', 'grid-row': '2', 'margin-top': '10px'}  # Ajustez la marge ou d'autres styles si nécessaire
        ),
    ]
)




def createCsvFile(apiURL):
    getCsvByLink.get_and_save_csv(apiURL, "data/dynamicData.csv") 
    
def main():
    createCsvFile("https://data.cdc.gov/api/views/9bhg-hcku/rows.csv?accessType=DOWNLOAD")
    app.run_server(debug=True)

if __name__ == "__main__":
    main()


