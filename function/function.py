import pandas as pd

#Fonction qui permet de créer un dataframe pour l'histogramme
def createHistoDf(df, filter):
    result = df.loc[(df['Group'] == 'By Total') & (df['State'] == filter) & (df['Sex'] == 'All Sexes') & (df['Age Group'] != 'All Ages')]
    columnToKeep = ['Age Group', 'COVID-19 Deaths','Total Deaths' ]
    result = result[columnToKeep]
    return result

#Fonction qui permet d'avoir la liste des états
def getAllState(CsvDataFrame):
    all_states = CsvDataFrame['State'].unique()
    return all_states

#Fonction qui convertie le numéro du slider en nom de colonne
def getSliderValueName(number):
    if number == 1:
        return 'Total Deaths'
    elif number == 2:
        return 'COVID-19 Deaths'
    elif number == 3:
        return 'Pneumonia Deaths'
    elif number == 4:
        return 'Pneumonia and COVID-19 Deaths'
    elif number == 5:
        return 'Influenza Deaths'
    elif number == 6:
        return 'Pneumonia, Influenza, or COVID-19 Deaths'
    
#Fonction qui permet de créer un dataframe pour la map
def createMapDf(df, filter):
    result = df.loc[(df['Group'] == 'By Total') & (df['State'] != 'United States') & (df['Sex'] == 'All Sexes') & (df['Age Group'] == 'All Ages')]
    columnToKeep = ['State',filter]
    result = result[columnToKeep]
    etats = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia',
             'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine',
             'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada',
             'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon',
             'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia',
             'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'Puerto Rico']
    #Code état pour la map utlisé dans Dash
    codes_etats = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS',
                   'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC',
                   'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY', 'PR']
    df_codes = pd.DataFrame({'State': etats, 'code': codes_etats})
    result = pd.merge(result, df_codes, on='State')
    return result