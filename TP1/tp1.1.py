# -*- coding: utf-8 -*-

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import glob

class CoinCounter:

    def __init__(self, imagePath, name='Image'):
        self.imageName = name
        self.imageOriginal = cv.imread(imagePath)
        self.__workingImage = cv.cvtColor(self.imageOriginal, cv.COLOR_BGR2GRAY)
        self.__imageCircles = cv.cvtColor(self.imageOriginal, cv.COLOR_BGR2GRAY)
       # self.__workingImage =self.imageOriginal
        self.__preProcessed = False           
        self.__edges = np.array([])
        self.__thresh = np.array([])
        self.__contours = np.array([])
        self.__circles = np.array([])
        self.__correctContours = []
        

        self.valores = {
                1 : (6000,11000),
                2 : (11000,14500),
                5 : (16000,17800),
                10 : (14500,16000),
                20 : (17800,19600),
                50 : (21500,25000) ,
                100 : (19600,21500) ,
                200 : (25000,30000)
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
        imgC = cv.drawContours(self.imageOriginal, self.__correctContours, -1, (0,0,255),2)
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
        self.__getContourCoords()
        total = 0

        for i in   self.__correctContours:
            M = cv.moments(i)
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
          
            for j in self.valores:
                if (cv.contourArea(i) >= self.valores[j][0] and cv.contourArea(i) <= self.valores[j][1]):
            
                    total += j
                    print(total)
                    #cv.putText(self.imageOriginal, f"{cv.contourArea(i)}",(cX,cY), cv.FONT_HERSHEY_SIMPLEX , 1, (0,0,255), 2)
                    cv.putText(self.imageOriginal, f"{j}",(cX,cY), cv.FONT_HERSHEY_SIMPLEX , 1, (0,0,255), 2)

        cv.putText(self.imageOriginal, f"total: {total}",(50,50), cv.FONT_HERSHEY_SIMPLEX , 1, (0,0,255), 2)

        



    def __getContourCoords(self):
        
        contours = self.__contours[0]
        print
        h = self.__contours[1]
    #    contourPoints = np.array([])
        a=0
        for cont in range (len(contours)):
           # contours[cont]
            leftmost = (contours[cont][contours[cont][:,:,0].argmin()][0])
            rightmost = (contours[cont][contours[cont][:,:,0].argmax()][0])
            topmost = (contours[cont][contours[cont][:,:,1].argmin()][0])
            bottommost = (contours[cont][contours[cont][:,:,1].argmax()][0])
            points = (leftmost,rightmost,topmost,bottommost)
            #self.__contourCords[cont] = points
            #center = (int((leftmost+rightmost)/2),(int((topmost+bottommost)/2))
        
            centerX = (leftmost[0]+rightmost[0])/2
            centerY = (topmost[1]+bottommost[1])/2
            radius = abs((rightmost[0]-leftmost[0])/2)
            area_circulo = round(np.pi * radius * radius,2) # area do circulo
            area_contour = cv.contourArea(contours[cont])
          #  cv.putText(self.imageOriginal, f"{c}",( int(centerX),int(centerY)), cv.FONT_HERSHEY_SIMPLEX , 1, (0,0,255), 2) 

            if (abs(area_circulo-area_contour)<2000 and h[0][cont][2] == -1  and area_contour>600 ):
               
              #  cv.putText(self.imageOriginal, f"{area_contour}",( int(centerX),int(centerY)), cv.FONT_HERSHEY_SIMPLEX , 1, (0,0,255), 2)
                a=a+1
              #  print("area",area_contour)
              #  print(a)
                
                self.__correctContours.append(contours[cont])
            
    
    def __detectEdges(self):
        self.__edges = cv.Canny(self.__workingImage,70,200)
        self.__thresh = cv.adaptiveThreshold(self.__edges, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 0)
        
        strElem = cv.getStructuringElement(cv.MORPH_ELLIPSE,(2,2))
        morph = cv.morphologyEx(self.__thresh,cv.MORPH_CLOSE,strElem,iterations=3) ## ajuda com os objetos que se toquem 3
        self.__contours = cv.findContours(morph,cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

        
        
        
        print(f'Thresh info\n {self.__thresh.dtype} {self.__thresh.shape}')
  

if __name__ == '__main__':
    fileDir = "TP1/PIV_20_21_TL1_imagens_treino/"
    imagesPath = glob.glob(f'{fileDir}*.jpg')
    
    c1 = CoinCounter(imagesPath[7], 'img1')
    c1.showImageOriginal()
    c1.preProcessImage(False)
    c1.showImageProcessed('P1')
    c1.countCoins()
    c1.showImageProcessed('Count')
    c1.showThresholds('P2')
    c1.showContors('Contors')