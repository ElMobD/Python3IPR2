import requests
import csv
from io import StringIO
import os

def get_and_save_csv(api_url, destination_path):
    if os.path.exists(destination_path):
        return
    
    response = requests.get(api_url, stream=True)    
    
    if response.status_code == 200:
        # Utilisez StringIO pour lire le texte CSV dans un objet file-like
        csv_data = StringIO(response.text)

        # Utilisez le module CSV pour lire les données depuis StringIO et les écrire dans un fichier CSV local
        with open(destination_path, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            
            # Écrivez chaque ligne du CSV dans le fichier
            for row in csv.reader(csv_data):
                csv_writer.writerow(row)
    else:
        print(f"Échec du téléchargement. Code de statut : {response.status_code}")
