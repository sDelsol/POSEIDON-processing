#-------------------------------------------------------------------------------
# Name:        Extract GNGGA
# Purpose: Extract GPS coordinates from a GNGGA frame in an ascii file and compile them in an other csv file
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
"""
Created on Mon Feb 13 10:02:13 2023

@author: Delta
"""

# Importer le module pandas qui sert de traitement DataFrame et importation du fichier
import pandas as pd

# Nom du fichier CSV
filename = "C:\\Users\\Delta\\Desktop\\Stage_M2\\20230607_Hermitage\\PM\\Positions_GNGGA_20230607_PM.csv"

# Lire le fichier CSV avec pandas
df = pd.read_csv(filename)

# Extraire les colonnes souhaitées dans le fichier csv SWMaps
cols = [1, 3, 4, 5, 6, 9]
filtered_df = df.iloc[:, cols]

# Afficher le nouveau DataFrame filtré
print(filtered_df)

filtered_df.to_csv("C:\\Users\\Delta\\Desktop\\Stage_M2\\20230607_Hermitage\\PM\\Pos_GPS_20230607_PM.csv", index=False)