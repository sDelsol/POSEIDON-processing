#-------------------------------------------------------------------------------
# Name:        Extract GNGGA
# Purpose: Extract GNGGA rows in a GPS ascii file and compile them in an other csv file
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
"""
Created on Mon Feb 13 09:57:09 2023

@author: Delta
"""

# Import the pandas module used for DataFrame processing and import the file
import pandas as pd

# Read all lines in the csv file
with open("C:\\Users\\Delta\\Desktop\\Stage_M2\\20230607_Hermitage\\PM\\SFE_Facet_230607_113553.ubx","r",encoding='ANSI') as file :
        lines=file.readlines()

# Filter GNGGA lines
filtered_lines=[line for line in lines if line.startswith("$GNGGA")]

# Create a pandas DataFrame from the extracted rows
df = pd.DataFrame(filtered_lines)

# Save as a new csv file
df.to_csv("C:\\Users\\Delta\\Desktop\\Stage_M2\\20230607_Hermitage\\PM\\Positions_GNGGA_20230607_PM.csv", header=None, lineterminator='\n')