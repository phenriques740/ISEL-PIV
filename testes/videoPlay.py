# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 12:02:55 2020

@author: pedro

teste em aula para correr videos
"""

import cv2

ratio = 4

imgDir = '../imageDatabase/'
videoName = 'video.mp4'

videoPath = imgDir + videoName

video = cv2.VideoCapture(videoPath)

while(video.isOpened()):
    ret, frame = video.read()

    h, w, layers = frame.shape
    new_h = h/ratio
    new_w = w/ratio

    newFrame= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #newFrame = cv2.resize(frame, (round(new_h) , round(new_w)))
    

    cv2.imshow('frame',newFrame)
    
    if (cv2.waitKey(1) & 0xFF == ord('q')) or cv2.getWindowProperty('frame',0)==-1:
        break
        
video.release()
cv2.destroyAllWindows()


