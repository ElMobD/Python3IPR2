from data import test
import pandas as pd
import csv

def main():
    apiURL = "https://data.transportation.gov/api/views/keg4-3bc2/rows.csv?accessType=DOWNLOAD"
    test.get_and_save_csv(apiURL, "dynamicData.csv") #Création du fichier CSV via le lien fourni au dessus
    
if __name__ == "__main__":
    main()