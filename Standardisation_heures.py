#-------------------------------------------------------------------------------
# Name:        Hours standardization
# Purpose: Gives the rightful format for time (HHMMSS to HH:MM:SS)
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
"""
Created on Tue May  2 10:12:36 2023

@author: Delta
"""

import csv

# Ouvrir le fichier CSV et lire son contenu
with open('C:\\Users\\Delta\\Desktop\\Stage_M2\\20230607_Hermitage\\PM\\Pos_GPS_20230607_PM_hhmmss.txt', 'r') as csvfile:
    reader = csv.reader(csvfile)
    # Lire la ligne d'en-tête
    header = next(reader)
    # Créer une nouvelle liste pour stocker les lignes modifiées
    modified_rows = []
    # Boucle sur chaque ligne du fichier CSV
    for row in reader:
        # Extrait la valeur de la première colonne de la ligne actuelle
        hhmmss = row[0]
        # Convertir le format de l'heure de HHMMSS à HH:MM:SS
        hh = hhmmss[0:2]
        mm = hhmmss[2:4]
        ss = hhmmss[4:6]
        new_time_format = f"{hh}:{mm}:{ss}"
        # Modifier la ligne actuelle avec le nouveau format d'heure
        row[0] = new_time_format
        # Ajouter la ligne modifiée à la liste des lignes modifiées
        modified_rows.append(row)

# Écrire les lignes modifiées dans le fichier CSV
with open('C:\\Users\\Delta\\Desktop\\Stage_M2\\20230607_Hermitage\\PM\\Pos_GPS_20230607_PM_v1.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    # Écrire la ligne d'en-tête
    writer.writerow(header)
    # Écrire les lignes modifiées
    writer.writerows(modified_rows)