#-------------------------------------------------------------------------------
# Name:        Extract GNGGA
# Purpose: Extract GPS coordinates from a GNGGA frame in an ascii file and compile them in an other csv file
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
"""
Created on Mon Feb 13 10:02:13 2023

@author: Delta
"""

# Import the pandas module used for DataFrame processing and import the file
import pandas as pd

# CSV file name
filename = "C:\\Users\\Delta\\Desktop\\Stage_M2\\TestPercheGoPro.csv"

# Read CSV file with pandas
df = pd.read_csv(filename)

# Extract the desired columns from SWMaps csv file
cols = [1, 3, 4, 5, 6, 9]
filtered_df = df.iloc[:, cols]

# Display the new filtered DataFrame
print(filtered_df)

filtered_df.to_csv("C:\\Users\\Delta\\Desktop\\Stage_M2\\TestPerche.csv", index=False)