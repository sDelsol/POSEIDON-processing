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

# Spécifier le répertoire contenant les images à renommer
input_folder = "C:\\Users\\Delta\\Desktop\\Stage_M2\\20230607_Hermitage\\PM\\Images_extraites\\QuartSec\\1G"

# Spécifier le préfixe à ajouter au nom des fichiers
prefix = "1G_"

# Spécifier le répertoire où vous souhaitez enregistrer les nouveaux fichiers
output_folder = "C:\\Users\\Delta\\Desktop\\Stage_M2\\20230607_Hermitage\\PM\\Images_extraites\\QuartSec\\1G"

# Parcourer tous les fichiers dans le dossier d'entrée
for filename in os.listdir(input_folder):

    # Vérifier si le fichier est une image
    if filename.endswith(".jpg") or filename.endswith(".png"):

        # Créer le nouveau nom de fichier en ajoutant le préfixe au nom existant
        new_filename = prefix + filename

        # Créer le chemin d'accès complet pour l'ancien fichier et le nouveau fichier
        old_path = os.path.join(input_folder, filename)
        new_path = os.path.join(output_folder, new_filename)

        # Renommer le fichier en déplaçant le fichier vers le nouveau chemin d'accès
        os.rename(old_path, new_path)

print("Toutes les images sont renommées avec succès ! Derien.")