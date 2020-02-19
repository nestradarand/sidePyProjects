#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 13:07:33 2020

@author: brento
"""

import cv2
import os
import numpy as np

# Get user supplied values
dirs = os.listdir(path)
imagePath = path
cascPath = "haarcascade_frontalface_default.xml"

other_files = ['.DS_Store', 'face_rec.py', 'haarcascade_frontalface_default.xml', 'faces']

dirs = os.listdir(path)

for item in dirs:
    if item not in other_files:
        # Create the haar cascade
        faceCascade = cv2.CascadeClassifier(cascPath)
        
        # Read the image
        image = cv2.imread(item)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Detect faces in the image
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.05,
            minNeighbors=5,
            minSize=(30, 30),
            flags = cv2.CASCADE_SCALE_IMAGE
        )
        
        print("Found {0} faces!".format(len(faces)))
        
        image_copy = np.copy(image)
        
        # Draw a rectangle around the faces
        face_crop = []
        for f in faces:
            x, y, w, h = [ v for v in f ]
            cv2.rectangle(image_copy, (x,y), (x+w, y+h), (255,0,0), 3)
            # Define the region of interest in the image  
            face_crop.append(gray[y:y+h, x:x+w])
        
        for i in range(0,len(face_crop)):
            cv2.imwrite(write_path + item + "_face" + str(i+1) + ".jpg", np.uint8(face_crop[i]))
        cv2.waitKey(0)

#for face in face_crop:
#    cv2.imshow('face',face)
#    cv2.waitKey(10)
    
#        for (x, y, w, h) in faces:
#            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
#        
#        cv2.imshow("Faces found", image)
#        cv2.waitKey(0