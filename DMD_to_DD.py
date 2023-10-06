#-------------------------------------------------------------------------------
# Name:        Converting GPS Coordinates
# Purpose: Compute and correct the lat and long coordinates from Decimal Minute Degree (ubx format) to Decimal Degree (used by photogrammetric softwares)
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
"""
Created on Tue May  9 10:12:49 2023

@author: Delta
"""
import csv


def convert_dmd2dd(number):
    # Diviser le nombre original (ex : 2104.XXXX) par 100 pour obtenir le degré correct (ex : 21.O4XXX)
    number /= 100
    # Isoler les minutes décimales
    decimal = number - int(number)
    # Multiplier les minutes décimales pour passer de 00.04XXX à 4.XXX
    decimal *= 100
    # Diviser les minutes décimales pour obtenir les décimales réelles
    decimal /= 60
    decimal = round(decimal, 8)
    # Écrire les données correctes en degrés décimaux
    return int(number) + decimal

# Ouvrir le fichier CSV et lire son contenu 
with open('C:\\Users\\Delta\\Desktop\\Stage_M2\\20230607_Hermitage\\PM\\Pos_GPS_20230607_PM_v1.csv', 'r') as infile :
    reader = csv.reader(infile)
    # Read the header row
    header = next(reader)
    
# Écrire les lignes modifiées dans le fichier CSV
with open('C:\\Users\\Delta\\Desktop\\Stage_M2\\20230607_Hermitage\\PM\\Pos_GPS_20230607_PM_vf.csv', 'w', newline='') as outfile:  
    writer = csv.writer(outfile)
    # Écrire la ligne d'en-tête
    writer.writerow(header)
    
    # Écrire les lignes modifiées avec le format de coordonnées correct
    for row in reader:
        updated_row = row.copy()
        for i in range(1, 3):
            number = float(row[i])
            updated_number = convert_dmd2dd(number)
            updated_row[i] = updated_number
        
        writer.writerow(updated_row)
