# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 14:48:09 2020

@author: pedro
"""
import cv2
import numpy as np

try:
    imgDir = '../imageDatabase/'
    imgPath = imgDir+'JonquilFlowers.jpg'
    
    img = cv2.imread(imgPath)
    imgg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)   
    
    cv2.imshow('Original', img)
    
    thres, bw = cv2.threshold(imgg,127,255,cv2.THRESH_BINARY_INV)
    
    cv2.imshow('BW Image' , bw)
    
    cont, b = cv2.findContours(bw, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    cnt = cont[4]
    cv2.drawContours(img,cont,-1, (0,0,255),3)
    
    bw = np.zeros(bw.shape, dtype=np.uint8)
    cv2.imshow('Countors' , img)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
except Exception as e:
    print('EXCEPT')
    cv2.destroyAllWindows()