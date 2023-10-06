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

# Open the CSV file and read its contents
with open('C:\\Users\\Delta\\Desktop\\Stage_M2\\20230607_Hermitage\\PM\\Pos_GPS_20230607_PM_hhmmss.txt', 'r') as infile:
    reader = csv.reader(infile)
    # Read the header row
    header = next(reader)
    # Create a new list to store the modified rows
    modified_rows = []
    # Loop through each row in the CSV file
    for row in reader:
        # Extract the value in the first column of the current row
        hhmmss = row[0]
        # Convert the time format from HHMMSS to HH:MM:SS
        hh = hhmmss[0:2]
        mm = hhmmss[2:4]
        ss = hhmmss[4:6]
        new_time_format = f"{hh}:{mm}:{ss}"
        # Modify the current row with the new time format
        row[0] = new_time_format
        # Append the modified row to the list of modified rows
        modified_rows.append(row)

# Write the modified rows back to the CSV file
with open('C:\\Users\\Delta\\Desktop\\Stage_M2\\20230607_Hermitage\\PM\\Pos_GPS_20230607_PM_v1.csv', 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    # Write the header row
    writer.writerow(header)
    # Write the modified rows
    writer.writerows(modified_rows)