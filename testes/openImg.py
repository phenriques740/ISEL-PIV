# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 11:43:57 2020

@author: pedro

Teste em aula para abrir imagem
"""


import cv2

imgDir = '../imageDatabase/'
imgName = 'falcon.jpg'


imgPath = imgDir+imgName


img = cv2.imread(imgPath)

if(img is None):
    print('Img is none')
    quit()

cv2.imshow('img', img)

cv2.waitKey(0)
cv2.destroyAllWindows()