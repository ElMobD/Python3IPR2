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
               
            ]
        ),
        html.Div(
            id='button-container',
            style={'flex':'1','width': '20%', 'display': 'flex', 'align-items': 'center', 'justify-content': 'space-between'},
            children=[
                html.Button(
                    'Histogramme',
                    style={}
                ),
                html.Button(
                    'Map',
                    style={}
                )
            ]
        )
    ]
)
    
def createCsvFile(apiURL):
    #Création du fichier CSV via le lien fourni au dessus
    getCsvByLink.get_and_save_csv(apiURL, "data/dynamicData.csv") 
    
def launchApp():
    app.run_server(debug=True)

def main():
    createCsvFile("https://data.cdc.gov/api/views/9bhg-hcku/rows.csv?accessType=DOWNLOAD")
    launchApp()

if __name__ == "__main__":
    main()



#HISTOGRAME abcise => âge & ordonnée => nombre morts totale et nombre mort covid
#MAP 