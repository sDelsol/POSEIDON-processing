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
    print("Worker 1 started")
    # Insert the first program here
    
    import cv2
    import time
    import os

    def video_to_frames(input_loc, output_loc, frame_nums):
            #input_loc: Input video file.
            #output_loc: Output directory to save the frames.
            #frame_nums: List of frame numbers to extract.
        
        try:
            os.mkdir(output_loc)
        except OSError:
            pass
        # Log the time
        time_start = time.time()
        # Start capturing the feed
        cap = cv2.VideoCapture(input_loc)
        # Find the number of frames
        video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
        print ("Number of frames: ", video_length)
        count = 0
        print ("Converting video..\n")
        # Start converting the video
        for frame_num in frame_nums:
            # Set the position of the next frame to read
            cap.set(cv2.CAP_PROP_POS_FRAMES, frame_num)
            # Extract the frame
            ret, frame = cap.read()
            if not ret:
                continue
            # Write the result back to output location.
            cv2.imwrite(output_loc + "/%#05d.jpg" % (frame_num), frame)
            count += 1
        # Log the time again
        time_end = time.time()
        # Release the feed
        cap.release()
        # Print stats
        print ("Done extracting frames.\n%d frames extracted" % count)
        print ("It took %d seconds for extraction." % (time_end-time_start))
        print ("Extracted frames: ", frame_nums)

    if __name__=="__main__":
        input_loc = 'C:\\Users\\Delta\\Desktop\\Stage_M2\\20230607_Hermitage\\PM\\2D\\GX010002.mp4'
        output_loc = 'C:\\Users\\Delta\\Desktop\\Stage_M2\\20230607_Hermitage\\PM\\Images_extraites\\QuartSeC\\2D'
        frame_nums = [0,24,48] # Example of a list of frames to be extracted
        video_to_frames(input_loc, output_loc, frame_nums)
    print("Worker 1 finished")

def worker2():
    print("Worker 2 started")
    # Insert the second program here
    
    import cv2
    import time
    import os

    def video_to_frames(input_loc, output_loc, frame_nums):
            #input_loc: Input video file.
            #output_loc: Output directory to save the frames.
            #frame_nums: List of frame numbers to extract.
        
        try:
            os.mkdir(output_loc)
        except OSError:
            pass
        # Log the time
        time_start = time.time()
        # Start capturing the feed
        cap = cv2.VideoCapture(input_loc)
        # Find the number of frames
        video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
        print ("Number of frames: ", video_length)
        count = 0
        print ("Converting video..\n")
        # Start converting the video
        for frame_num in frame_nums:
            # Set the position of the next frame to read
            cap.set(cv2.CAP_PROP_POS_FRAMES, frame_num)
            # Extract the frame
            ret, frame = cap.read()
            if not ret:
                continue
            # Write the result back to output location.
            cv2.imwrite(output_loc + "/%#05d.jpg" % (frame_num+12840), frame)
            count += 1
        # Log the time again
        time_end = time.time()
        # Release the feed
        cap.release()
        # Print stats
        print ("Done extracting frames.\n%d frames extracted" % count)
        print ("It took %d seconds for extraction." % (time_end-time_start))
        print ("Extracted frames: ", frame_nums)

    if __name__=="__main__":
        input_loc = 'C:\\Users\\Delta\\Desktop\\Stage_M2\\20230607_Hermitage\\PM\\2D\\GX020002.mp4'
        output_loc = 'C:\\Users\\Delta\\Desktop\\Stage_M2\\20230607_Hermitage\\PM\\Images_extraites\\QuartSeC\\2D'
        frame_nums = [0,24,48] # Example of a list of frames to be extracted
        video_to_frames(input_loc, output_loc, frame_nums)
    print("Worker 2 finished")

def worker3():
    print("Worker 3 started")
    # Insert the third program here
    
    import cv2
    import time
    import os

    def video_to_frames(input_loc, output_loc, frame_nums):
            #input_loc: Input video file.
            #output_loc: Output directory to save the frames.
            #frame_nums: List of frame numbers to extract.
        
        try:
            os.mkdir(output_loc)
        except OSError:
            pass
        # Log the time
        time_start = time.time()
        # Start capturing the feed
        cap = cv2.VideoCapture(input_loc)
        # Find the number of frames
        video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
        print ("Number of frames: ", video_length)
        count = 0
        print ("Converting video..\n")
        # Start converting the video
        for frame_num in frame_nums:
            # Set the position of the next frame to read
            cap.set(cv2.CAP_PROP_POS_FRAMES, frame_num)
            # Extract the frame
            ret, frame = cap.read()
            if not ret:
                continue
            # Write the result back to output location.
            cv2.imwrite(output_loc + "/%#05d.jpg" % (frame_num+25632), frame)
            count += 1
        # Log the time again
        time_end = time.time()
        # Release the feed
        cap.release()
        # Print stats
        print ("Done extracting frames.\n%d frames extracted" % count)
        print ("It took %d seconds for extraction." % (time_end-time_start))
        print ("Extracted frames: ", frame_nums)

    if __name__=="__main__":
        input_loc = 'C:\\Users\\Delta\\Desktop\\Stage_M2\\20230607_Hermitage\\PM\\2D\\GX030002.mp4'
        output_loc = 'C:\\Users\\Delta\\Desktop\\Stage_M2\\20230607_Hermitage\\PM\\Images_extraites\\QuartSeC\\2D'
        frame_nums = [0,24,48] # Example of a list of frames to be extracted
        video_to_frames(input_loc, output_loc, frame_nums)
    print("Worker 3 finished")

def worker4():
    print("Worker 4 started")
    # Insert the fourth program here
    
    import cv2
    import time
    import os

    def video_to_frames(input_loc, output_loc, frame_nums):
            #input_loc: Input video file.
            #output_loc: Output directory to save the frames.
            #frame_nums: List of frame numbers to extract.
        
        try:
            os.mkdir(output_loc)
        except OSError:
            pass
        # Log the time
        time_start = time.time()
        # Start capturing the feed
        cap = cv2.VideoCapture(input_loc)
        # Find the number of frames
        video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
        print ("Number of frames: ", video_length)
        count = 0
        print ("Converting video..\n")
        # Start converting the video
        for frame_num in frame_nums:
            # Set the position of the next frame to read
            cap.set(cv2.CAP_PROP_POS_FRAMES, frame_num)
            # Extract the frame
            ret, frame = cap.read()
            if not ret:
                continue
            # Write the result back to output location.
            cv2.imwrite(output_loc + "/%#05d.jpg" % (frame_num+38418), frame)
            count += 1
        # Log the time again
        time_end = time.time()
        # Release the feed
        cap.release()
        # Print stats
        print ("Done extracting frames.\n%d frames extracted" % count)
        print ("It took %d seconds for extraction." % (time_end-time_start))
        print ("Extracted frames: ", frame_nums)

    if __name__=="__main__":
        input_loc = 'C:\\Users\\Delta\\Desktop\\Stage_M2\\20230607_Hermitage\\PM\\2D\\GX040002.mp4'
        output_loc = 'C:\\Users\\Delta\\Desktop\\Stage_M2\\20230607_Hermitage\\PM\\Images_extraites\\QuartSeC\\2D'
        frame_nums = [0,24,48] # Example of a list of frames to be extracted
        video_to_frames(input_loc, output_loc, frame_nums)
    print("Worker 4 finished")


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