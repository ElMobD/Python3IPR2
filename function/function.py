import pandas as pd

def createHistoDf(df, filter):
    result = df.loc[(df['Group'] == 'By Total') & (df['State'] == filter) & (df['Sex'] == 'All Sexes') & (df['Age Group'] != 'All Ages')]
    columnToKeep = ['Age Group', 'COVID-19 Deaths','Total Deaths' ]
    result = result[columnToKeep]
    return result

def getAllState(CsvDataFrame):
    all_states = CsvDataFrame['State'].unique()
    return all_states

def createMapDf(df):
    result = df.loc[(df['Group'] == 'By Total') & (df['State'] != 'United States') & (df['Sex'] == 'All Sexes') & (df['Age Group'] == 'All Ages')]
    columnToKeep = ['State','Total Deaths']
    result = result[columnToKeep]
    etats = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia',
             'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine',
             'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada',
             'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon',
             'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia',
             'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', 'Puerto Rico']
    codes_etats = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS',
                   'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC',
                   'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY', 'PR']
    df_codes = pd.DataFrame({'State': etats, 'code': codes_etats})
    result = pd.merge(result, df_codes, on='State')
    return result