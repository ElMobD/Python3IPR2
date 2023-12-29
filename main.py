from data import getCsvByLink
import pandas as pd


def createCsvFile():
    apiURL = "https://data.cdc.gov/api/views/9bhg-hcku/rows.csv?accessType=DOWNLOAD"
    #Création du fichier CSV via le lien fourni au dessus
    getCsvByLink.get_and_save_csv(apiURL, "dynamicData.csv") 
    
def main():
    createCsvFile()

if __name__ == "__main__":
    main()



#HISTOGRAME abcise => âge & ordonnée => nombre morts totale et nombre mort covid
#MAP 