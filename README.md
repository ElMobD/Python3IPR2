Projet Python réalisé en 2023 dans le cadre de l'unité Python en E3 à l'ESIEE Paris durant le cycle Ingénieur Informatique et Application 3D



Données utilisées :



lien de téléchargement du fichier CSV : https://data.cdc.gov/api/views/9bhg-hcku/rows.csv?accessType=DOWNLOAD

utilisation de code d'état d'Amérique





# USER GUIDE



Prérequis : Installation de python sur votre machine et du module pip



1. Clonez le projet via cette commande : 'git clone https://github.com/ElMobD/Python3IPR2.git' ou télécharger le projet zip depuis le même lien fourni puis le dézipper



2. Installer les packages additionnels via cette commande : 'python -m pip install -r requirements.txt'



3. Aller dans le terminal (ou console) et se déplacer dans le dossier où se trouve le fichier main.py. Exécuter la commande : 'python main.py'



4. Pour ouvrir le projet après avoir fait l'étape d'au-dessus, copier-coller l'adresse locale créée sur la barre de recherche de votre navigateur web



5. Vous pouvez désormais voir le Dashboard ! Ne pas fermer la console de comm

Quand l'application se lance, le fichier CSV est créé à partir de ce lien : https://data.cdc.gov/api/views/9bhg-hcku/rows.csv?accessType=DOWNLOAD
La première fois que l'application se lance, cela peut prendre du temps. Mais une fois le fichier CSV créer dans le projet, l'applicaiton ne prendra normalement plus du temps au lancement. 

# DEVELOPPER GUIDE

- Le projet contient un fichier main.py qui doit être exécuté pour lancer l'application Dash. 
- Il contient un fichier ReadME.md
- Il contient un fichier requirements.txt qui contient les packages additionnels à installer
- Il contient un dossier data qui contient un fichier getCsvByLink.py qui récupère un fichier CSV via un lien et recréer un fichier CSV en local. 
- dynamicData.csv est le fichier créé par le fichier getCsvByLink.py et dynamicData2.csv est le fichier a utilisé au cas où le fichier getCsvByLink.py n'arriverait pas à créer le premier fichier CSV
- Il contient un dossier function qui contient un fichier function.py qui contient plusieurs fonctions utilisées dans tous le projet (C'est que sont créé les dataFrames qui sont utilisé pour faire les figures)


# RAPPORT D'ANALYSE

Les données appartiennent à : https://data.cdc.gov/

Le sujet traité est le nombre de morts dans tous les États-Unis causé par la COVID-19, Pneumonie, Influenza ou bien le nombre de morts total.
Le jeu de données utilisées offre un aperçu des statistiques de mortalité aux États-Unis, couvrant la période du 1er janvier 2020 au 23 septembre 2023.
Il englobe divers facteurs démographiques tels que les groupes d'âge, le sexe et les distinctions géographiques, offrant une perspective nuancée sur l'impact de la COVID-19 et des affections respiratoires connexes. Ce rapport vise à analyser et à interpréter les données, mettant en lumière les tendances, schémas et disparités dans les taux de mortalité au sein de différents segments de la population.
En explorant les détails complexes des décès liés à la COVID-19, aux pneumonies et à leurs intersections, cette analyse cherche à apporter des éclairages précieux sur le paysage de la santé publique au cours de cette période cruciale.

L'histogramme : L'histogramme présente le nombre total de morts dans chaque état en comparaison avec le nombre de morts causé par la COVID-19 par groupe d'âge du 1er janvier 2020 au 23 septembre 2023.
Tout d'abord ce qui est flagrant quand on regarde l'histogramme, c'est que le nombre de morts causé par la COVID-19 est beaucoup plus petit que le nombre total de mort.
Et ceci peu importe si l'on sélectionne l'entièreté des États-Unis ou chaque état individuellement ou bien le groupe d'âge.
On peut voir que la plupart des personnes qui sont victimes de la COVID-19 sont âgées d'au moins 50 ans.
Ceci concorde bien avec ce que les médecins disent par rapport aux potentiel victimes de ce virus ( Les personnes âgées ).

La carte : La carte présente le nombre de morts causés par la COVID-19, la pneumonie, les 2 assemblés, la grippe, les 3 assemblés et le nombre total de morts dans tous les États-Unis et dans chaque état.
La carte nous permet de voir où il y a le plus de victime dans tous les états Unis.
Dans la globalité, on se rend compte que c'est dans les mêmes états qu'il y a le plus de victimes et ce peu importe le type de mort ou dans le nombre total de morts.
Il y a 3 états qui reviennent. La Californie, le Texas et la Floride. En recherchant pourquoi c'est assez logique.
En effet les 3 états où il y a le plus de morts sont en fait les états les plus peuplés.
Cela s'explique par le fait que d'une plus il y a du monde, plus y a de mort possible et d'autre que ces maladies sont facilement transmissible donc plus de cas possible.

En conclusion, ces différentes analyses nous montrent la véracité de la plupart des propos qui ont été déclaré par les Médecins du monde entier.
Pour améliorer le projet, l'utilisation d'autre données comme le nombre de cas où encore le nombre d'habitants par états auraient été très bénéfiques.
