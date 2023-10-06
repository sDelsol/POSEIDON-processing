#-------------------------------------------------------------------------------
# Name:        Extract GNGGA
# Purpose: Extract GNGGA rows in a GPS ascii file and compile them in an other csv file
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
"""
Created on Mon Feb 13 09:57:09 2023

@author: Delta
"""

# Importer le module pandas qui sert de traitement DataFrame et importation du fichier
import pandas as pd

# Lire toutes les lignes du fichier csv
with open("C:\\Users\\Delta\\Desktop\\Stage_M2\\20230607_Hermitage\\PM\\SFE_Facet_230607_113553.ubx","r",encoding='ANSI') as file :
        lines=file.readlines()

# Filtrer les lignes GNGGA
filtered_lines=[line for line in lines if line.startswith("$GNGGA")]

# Créer un DataFrame pandas à partir des lignes extraites
df = pd.DataFrame(filtered_lines)

# Enregistrer le tout dans un nouveau fichier csv
df.to_csv("C:\\Users\\Delta\\Desktop\\Stage_M2\\20230607_Hermitage\\PM\\Positions_GNGGA_20230607_PM.csv", header=None, lineterminator='\n')