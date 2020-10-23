# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 12:15:23 2020

@author: pedro
"""


import cv2


imgDir = '../imageDatabase/'
imgName = 'fingerprint.jpg'
imgResizedName = 'fingerprint2.jpg'

factor = 0.15
try:
    img = cv2.imread(imgDir + imgName)
    img2 = cv2.resize(img, (int(img.shape[1] * factor), int(img.shape[0] * factor)))
    
    
    cv2.imshow('Original', img2)
    
    Ifx = 5
    Ify = 5
    
    img3 = cv2.resize(img2, (0,0),fx = Ifx, fy = Ify, interpolation = cv2.INTER_CUBIC)
    img4 = cv2.resize(img2, (0,0),fx = Ifx, fy = Ify, interpolation = cv2.INTER_NEAREST)
    img5 = cv2.resize(img2, (0,0),fx = Ifx, fy = Ify, interpolation = cv2.INTER_LINEAR)        
    
    cv2.imshow('Img resize cubic' , img3)
    cv2.imshow('Img resize Nearest' , img4)
    cv2.imshow('img resize linear', img5)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
except Exception as e:
    print(e)
    cv2.destroyAllWindows()