#-------------------------------------------------------------------------------
# Name:        Extract frames - Multiprocessing version
# Purpose: Function to extract specific frames from input video file and save them as separate frames in an output directory without having to relaunch the code each time
# -*- coding: utf-8 -*-
# Disclaimer : for some reason unbeknownst to my person, the following code sometimes does not extract frames for the 2nd second of the video (frame number 24 to 47)
# Note : you can modify the following code to add more worker by copy-pasting one of the already defined worker
#-------------------------------------------------------------------------------
"""
Created on Wed Feb 15 04:24:53 2023

@author: Delta
"""

import psutil
print(psutil.cpu_count())

import multiprocessing

def worker1():
    print("Worker 1 démarré")
    # Insérer le quatrième programme
    
    import cv2
    import time
    import os

    def video_to_frames(input_loc, output_loc, frame_nums):
            #input_loc: Fichier vidéo en entrée.
            #output_loc: Répertoire de sortie pour enregistrer les images.
            #frame_nums: Liste des numéros d'image' à extraire.
        
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
            cv2.imwrite(output_loc + "/%#05d.jpg" % (frame_num+38418), frame)
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
        input_loc = 'C:\\Users\\Delta\\Desktop\\Stage_M2\\20230607_Hermitage\\PM\\2D\\GX040002.mp4'
        output_loc = 'C:\\Users\\Delta\\Desktop\\Stage_M2\\20230607_Hermitage\\PM\\Images_extraites\\QuartSeC\\2D'
        frame_nums = [0,24,48] # Example of a list of frames to be extracted
        video_to_frames(input_loc, output_loc, frame_nums)
    print("Worker 1 terminé")

def worker2():
    print("Worker 2 démarré")
    # Insérer le quatrième programme
    
    import cv2
    import time
    import os

    def video_to_frames(input_loc, output_loc, frame_nums):
            #input_loc: Fichier vidéo en entrée.
            #output_loc: Répertoire de sortie pour enregistrer les images.
            #frame_nums: Liste des numéros d'image' à extraire.
        
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
            cv2.imwrite(output_loc + "/%#05d.jpg" % (frame_num+38418), frame)
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
        input_loc = 'C:\\Users\\Delta\\Desktop\\Stage_M2\\20230607_Hermitage\\PM\\2D\\GX040002.mp4'
        output_loc = 'C:\\Users\\Delta\\Desktop\\Stage_M2\\20230607_Hermitage\\PM\\Images_extraites\\QuartSeC\\2D'
        frame_nums = [0,24,48] # Example of a list of frames to be extracted
        video_to_frames(input_loc, output_loc, frame_nums)
    print("Worker 2 terminé")

def worker3():
    print("Worker 3 démarré")
    # Insérer le quatrième programme
    
    import cv2
    import time
    import os

    def video_to_frames(input_loc, output_loc, frame_nums):
            #input_loc: Fichier vidéo en entrée.
            #output_loc: Répertoire de sortie pour enregistrer les images.
            #frame_nums: Liste des numéros d'image' à extraire.
        
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
            cv2.imwrite(output_loc + "/%#05d.jpg" % (frame_num+38418), frame)
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
        input_loc = 'C:\\Users\\Delta\\Desktop\\Stage_M2\\20230607_Hermitage\\PM\\2D\\GX040002.mp4'
        output_loc = 'C:\\Users\\Delta\\Desktop\\Stage_M2\\20230607_Hermitage\\PM\\Images_extraites\\QuartSeC\\2D'
        frame_nums = [0,24,48] # Example of a list of frames to be extracted
        video_to_frames(input_loc, output_loc, frame_nums)
    print("Worker 3 terminé")

def worker4():
    print("Worker 4 démarré")
    # Insérer le quatrième programme
    
    import cv2
    import time
    import os

    def video_to_frames(input_loc, output_loc, frame_nums):
            #input_loc: Fichier vidéo en entrée.
            #output_loc: Répertoire de sortie pour enregistrer les images.
            #frame_nums: Liste des numéros d'image' à extraire.
        
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
            cv2.imwrite(output_loc + "/%#05d.jpg" % (frame_num+38418), frame)
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
        input_loc = 'C:\\Users\\Delta\\Desktop\\Stage_M2\\20230607_Hermitage\\PM\\2D\\GX040002.mp4'
        output_loc = 'C:\\Users\\Delta\\Desktop\\Stage_M2\\20230607_Hermitage\\PM\\Images_extraites\\QuartSeC\\2D'
        frame_nums = [0,24,48] # Example of a list of frames to be extracted
        video_to_frames(input_loc, output_loc, frame_nums)
    print("Worker 4 terminé")


if __name__ == "__main__":
    # Launch each function one after tother
    p1 = multiprocessing.Process(target=worker1())
    p2 = multiprocessing.Process(target=worker2())
    p3 = multiprocessing.Process(target=worker3())
    p4 = multiprocessing.Process(target=worker4())
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    # Wait so that each process is over
    p1.join()
    p2.join()
    p3.join()
    p4.join()