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
    # Divide the original number (ex : 2104.XXXX) by a 100 to get the correct degree (ex : 21.O4XXX)
    number /= 100
    # Isolate decimal minutes
    decimal = number - int(number)
    # Multiply decimal minutes to pass from 00.04XXX to 4.XXX
    decimal *= 100
    # Divide the decimal minutes to obtain the real decimals
    decimal /= 60
    decimal = round(decimal, 8)
    # Write the correct data in Decimal Degree
    return int(number) + decimal

# Open the CSV file and read its contents 
with open('C:\\Users\\Delta\\Desktop\\Stage_M2\\20230607_Hermitage\\PM\\Pos_GPS_20230607_PM_v1.csv', 'r') as infile :
    reader = csv.reader(infile)
    # Read the header row
    header = next(reader)
    
# Write the modified rows back to the CSV file
with open('C:\\Users\\Delta\\Desktop\\Stage_M2\\20230607_Hermitage\\PM\\Pos_GPS_20230607_PM_vf.csv', 'w', newline='') as outfile:  
    writer = csv.writer(outfile)
    # Write the header row
    writer.writerow(header)
    
    # Write the modified rows with the correct coordinates format
    for row in reader:
        updated_row = row.copy()
        for i in range(1, 3):
            number = float(row[i])
            updated_number = convert_dmd2dd(number)
            updated_row[i] = updated_number
        
        writer.writerow(updated_row)
