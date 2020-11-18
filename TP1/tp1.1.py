# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 11:32:52 2020

@author: pedro
"""

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

class CoinCounter:
    def __init__(self, imagePath, name='Image'):
        self.imageOriginal = cv2.imread(imagePath)
        self.imageName = name
        
    def showImageOriginal(self):
        cv.imshow('Original ' ´+ str(self.name),self.image)
    
    def showImageProcessed(self):
       pass 
   
    
    def processImage(self):
    
    def __detectEdges(self):
        imgHeight, imgWidth, img_channel = coins.shape
        contours , heirachy = zip(*[ cv2.findContours(i, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) for i in thresh]) #contours

c1 = CoinCounter(5, 'img1')