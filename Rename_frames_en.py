#-------------------------------------------------------------------------------
# Name:        Rename frames
# Purpose: Attribute a prefix for each image so that the cameras do not get mixed up on Metashape
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
"""
Created on Wed Feb 22 14:04:42 2023

@author: Delta
"""

import os

# Specify the directory containing the images to be renamed
input_folder = "C:\\Users\\Delta\\Desktop\\Stage_M2\\20230607_Hermitage\\PM\\Images_extraites\\QuartSec\\1G"

# Specify the prefix to be added to file names
prefix = "1G_"

# Specify the directory where you wish to save the new files
output_folder = "C:\\Users\\Delta\\Desktop\\Stage_M2\\20230607_Hermitage\\PM\\Images_extraites\\QuartSec\\1G"

# Browse all files in the input folder
for filename in os.listdir(input_folder):

    # Check if the file is an image
    if filename.endswith(".jpg") or filename.endswith(".png"):

        # Create a new file name by adding the prefix to the existing name
        new_filename = prefix + filename

        # Create the full path for the old and new files
        old_path = os.path.join(input_folder, filename)
        new_path = os.path.join(output_folder, new_filename)

        # Rename the file by moving it to the new path
        os.rename(old_path, new_path)

print("All files renamed with success. You're welcome !")