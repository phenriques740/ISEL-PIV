# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 11:32:52 2020

@author: pedro
"""

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import glob

class CoinCounter:
    def __init__(self, imagePath, name='Image'):
        self.imageName = name

        self.imageOriginal = cv.imread(imagePath)
        self.__workingImage = cv.cvtColor(self.imageOriginal, cv.COLOR_BGR2GRAY)
        self.__preProcessed = False
                
        self.__edges = np.array([])
        self.__thresh = np.array([])
        self.__contours = np.array([])
        self.__circles = np.array([])
        
        
        self.valores = {
                1 : 0,
                2 : 0,
                5 : 0,
                10 : 427,
                20 : 490,
                50 : 0, 
                100 : 515,
                200 : 0
            }
        
    def __showImage(self, image, title):
        win_title= f'{self.imageName} {title}'
        cv.imshow(win_title, image)
        cv.waitKey(0)
        cv.destroyWindow(win_title)
        
    
    def showImageOriginal(self, text='original'):
        return self.__showImage(self.imageOriginal, text)
    
    def showImageProcessed(self, text='processed'):
        return self.__showImage(self.__workingImage,text )
    
    def showContors(self, text='contors'):
        imgC = cv.drawContours(self.imageOriginal, self.__contours[0], -1, (0,0,255))
        return self.__showImage(imgC, text)
    
    def showThresholds(self,text='edges'):
        return self.__showImage(self.__thresh, text)
        
   
    '''
    Faz um re-dimensionamento (se aplicavel) e aplica filtros para obter melhores resultado
    '''
    def preProcessImage(self,resize=False):
        w, h, a = self.imageOriginal.shape
        
        blur = []
        if(resize):
            img= cv.resize(self.__workingImage, (int(h/2), int(w/2)))
            blur=cv.GaussianBlur(img,(7,7),0)
        else:
            blur=cv.GaussianBlur(self.__workingImage,(7,7),0)
        
        self.__workingImage = blur
        self.__preProcessed = True
        return self.__preProcessed
    
    def countCoins(self):
        self.__detectEdges()
        
        contours = self.__contours[0]
        h = self.__contours[1]
        circles = []

        print(len(contours))
        for cont in contours:
            (x,y),radius = cv.minEnclosingCircle(cont)
            center = (int(x),int(y))
            radius = int(radius)
            area_circulo = np.pi * 2 * radius
            
            if(abs(cv.arcLength(cont,True) - area_circulo) <50):
                print('append circulos')
                circles.append(cont)
                
                cv.circle(self.__workingImage, center , int(radius), (0,0,255), thickness = 1)
            
        return 
        
        contornos=[]
        for c in range(len(cont)):
            
            circulo= 4 * np.pi * (cv.contourArea(cont[c]) / cv.arcLength(cont[c], True)**2)
            if circulo >= 0.7 and circulo <= 1 and h[0][c][2] == -1:
                contornos.append(c)
                print("c: ",c)
        
        
        for c in contornos:
                    area = cv.contourArea(cont[c])
                    if area < 5000:
                        contornos.remove(c)
        
        
        print("contornos",contornos)


            
    '''
    Deteta os circulos usando o algoritmo de Hough
    
    @return np.array(1, N, 3) onde N é o numero de circulos e 3 corresponde ao tuplo (posX , posY, raio)
    '''
    def __detectCircles(self):
        return cv.HoughCircles(self.__workingImage, cv.HOUGH_GRADIENT, 1.2, 5)
    
    def __detectEdges(self):
        self.__edges = cv.Canny(self.__workingImage,70,200)
        self.__thresh = cv.adaptiveThreshold(self.__edges, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 1)
        
        strElem = cv.getStructuringElement(cv.MORPH_ELLIPSE,(2,2))
        morph = cv.morphologyEx(self.__thresh,cv.MORPH_CLOSE,strElem,iterations=3) ## ajuda com os objetos que se toquem
        self.__contours = cv.findContours(morph,cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        
        
        
        print(f'Thresh info\n {self.__thresh.dtype} {self.__thresh.shape}')
        

if __name__ == '__main__':
    fileDir = "PIV_20_21_TL1_imagens_treino/"
    imagesPath = glob.glob(f'{fileDir}*.jpg')
    
    c1 = CoinCounter(imagesPath[7], 'img1')
    c1.showImageOriginal()
    c1.preProcessImage(False)
    c1.showImageProcessed('P1')
    c1.countCoins()
    c1.showImageProcessed('Count')
    #c1.showThresholds('P2')
    #c1.showContors('Contors')