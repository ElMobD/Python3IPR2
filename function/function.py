import pandas as pd

def createHistoDf(df, filter):
    result = df.loc[(df['Group'] == 'By Total') & (df['State'] == filter) & (df['Sex'] == 'All Sexes') & (df['Age Group'] != 'All Ages')]
    columnToKeep = ['Age Group', 'COVID-19 Deaths','Total Deaths' ]
    result = result[columnToKeep]
    return result

def getAllState(CsvDataFrame):
    all_states = CsvDataFrame['State'].unique()
    return all_states
