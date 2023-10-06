#-------------------------------------------------------------------------------
# Name:        Extract frames
# Purpose: Function to extract specific frames from input video file and save them as separate frames in an output directory
# -*- coding: utf-8 -*-
# Disclaimer : for some reason unbeknownst to my person, the following code sometimes does not extract frames for the 2nd second of the video (frame number 24 to 47)
#-------------------------------------------------------------------------------
"""
Created on Wed Feb 15 03:45:18 2023

@author: Delta
"""

import cv2
import time
import os

def video_to_frames(input_loc, output_loc, frame_nums):
        # input_loc: Fichier vidéo en entrée.
        # output_loc: Répertoire de sortie pour enregistrer les images.
        # frame_nums: Liste des numéros d'image' à extraire.
    
    try:
        os.mkdir(output_loc)
    except OSError:
        pass
    # Enregistrer l'heure
    time_start = time.time()
    # Commencer à capturer le flux
    cap = cv2.VideoCapture(input_loc)
    # Trouver le nombre d'images
    video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
    print ("Number of frames: ", video_length)
    count = 0
    print ("Converting video..\n")
    # Lancer la conversion de la vidéo
    for frame_num in frame_nums:
        # Définir la position de la prochaine image à lire
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_num)
        # Extraire l'image
        ret, frame = cap.read()
        if not ret:
            continue
        # Enregistrer l'image dans le répertoire de sortie
        cv2.imwrite(output_loc + "/%#05d.jpg" % (frame_num), frame)
        count += 1
    # Enregistrez à nouveau l'heure
    time_end = time.time()
    # Relâcher le flux
    cap.release()
    # Voir les statistiques
    print ("Fin de l'extraction.\n%d frames extraites" % count)
    print ("L'extraction a duré %d." % (time_end-time_start))
    print ("Images extraites: ", frame_nums)

if __name__=="__main__":
    input_loc = 'C:\\Users\\Delta\\Desktop\\Stage_M2\\20230607_Hermitage\\PM\\2D\\GX010001.mp4'
    output_loc = 'C:\\Users\\Delta\\Desktop\\Stage_M2\\20230607_Hermitage\\PM\\Images_extraites\\v1\\2D'
    frame_nums = [0,24,48] # Exemple de liste de frames à extraire
    video_to_frames(input_loc, output_loc, frame_nums)