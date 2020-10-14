# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 21:51:18 2020

@author: pedro

Chromakey
"""


import cv2

imgDir = '../imageDatabase/'
imgPath = imgDir+'falcon.jpg'
maskPath = imgDir+'mask.png'
backgroundPath = imgDir+'florest.jpg'


img = cv2.imread(imgPath)
mask = cv2.imread(maskPath)
background = cv2.imread(backgroundPath)


newImg = cv2.bitwise_and(img,mask) + cv2.bitwise_and(background,cv2.bitwise_not(mask))


cv2.imshow('originalImg',img)
cv2.imshow('mask',mask)

cv2.imshow('background',background)

cv2.imshow('Chroma key img', newImg)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('originalImg',newImg)


blurImg = cv2.blur(newImg, (10,10))
cv2.imshow('blurred Img' , blurImg)

medianBlur = cv2.medianBlur(newImg, 9) # perguntar porque valor de k % 2 tem de ser 1
cv2.imshow('medianBlur' , medianBlur)

gausianBlur = cv2.GaussianBlur(newImg, (5,5), 0)
cv2.imshow('gausianBlur' , gausianBlur)

cv2.waitKey(0)
cv2.destroyAllWindows()