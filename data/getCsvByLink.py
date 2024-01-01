import requests
import csv
from io import StringIO
import os

def get_and_save_csv(api_url, destination_path):
    if os.path.exists(destination_path): #si le fichier existe déjà, on ne le télécharge pas
        return
    
    response = requests.get(api_url, stream=True)    
    
    if response.status_code == 200:
        # Créez un objet StringIO contenant le texte brut de la réponse
        csv_data = StringIO(response.text)

        # Utilisez le module csv pour lire ce fichier StringIO dans un objet DictReader
        with open(destination_path, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            
            ## Pour chaque ligne du fichier CSV distant...
            for row in csv.reader(csv_data):
                csv_writer.writerow(row)
    else:
        print(f"Échec du téléchargement. Code de statut : {response.status_code}")
