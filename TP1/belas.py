import cv2 as cv
import numpy as np
import math

fileDir="PIV_20_21_TL1_imagens_treino/"
fileName="P1000710s.jpg"
imgcoins=cv.imread(fileDir+fileName)
cv.imshow("coins",imgcoins)
cv.waitKey(0)
cv.destroyAllWindows()



imgt=imgcoins.copy()

#imgt[:,:,0]=0

img=cv.cvtColor(imgt,cv.COLOR_BGR2GRAY)
blur=cv.GaussianBlur(img,(7,7),0)
canny=cv.Canny(blur,70,200)
##canny=cv.fastNlMeansDenoisingColored(imgcoins,None,10,10,7,21)



thres = cv.adaptiveThreshold(canny, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 1)
##print(thres)

cv.imshow("Thresh",thres)
cv.waitKey(0)
cv.destroyAllWindows()



##regionNum, lb=cv.connectedComponents(bw)
strElem=cv.getStructuringElement(cv.MORPH_ELLIPSE,(2,2))
bw1=cv.morphologyEx(thres,cv.MORPH_CLOSE,strElem,iterations=1)
cv.imshow("BW1Image",bw1)
##bw1=cv.dilate(bw,strElem)
##bw2=cv.erode(bw,strElem)
##cv.imshow('BW Morph Image 1',bw1)
##cv.imshow('BW Morph Image 2',bw2)

cont,h=cv.findContours(bw1,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
##print(len(cont))

teste=cv.cvtColor(bw1, cv.COLOR_GRAY2BGR)

##for c in range(len(cont)):
##    areat=cv.contourArea(cont[c])
##    if areat<5000:
##        cont.remove(c)
contornos=[]
for c in range(len(cont)):
    
    circulo= 4 * math.pi * (cv.contourArea(cont[c]) / cv.arcLength(cont[c], True)**2)
    if circulo >= 0.7 and circulo <= 1 and h[0][c][2] == -1:
        contornos.append(c)
        print("c: ",c)


for c in contornos:
            area = cv.contourArea(cont[c])
            if area < 5000:
                contornos.remove(c)


print("contornos",contornos)
valor=0.0
for contador in contornos:
    area=cv.contourArea(cont[contador])

        ##if(contador%2!=0 and contador!=0):
    if 7000 < area < 9000:
        print(contador)
        print("1 cêntimos")
        print(cv.contourArea(cont[contador]))
        cv.drawContours(teste,cont,contador,(0,0,255),thickness=2)
        cv.drawContours(imgcoins,cont,contador,(0,0,255),thickness=2)
        valor+=0.01

    if 9000 < area < 12000:
        print(contador)
        print("2 cêntimos")
        print(cv.contourArea(cont[contador]))
        cv.drawContours(teste,cont,contador,(0,0,255),thickness=2)
        cv.drawContours(imgcoins,cont,contador,(0,0,255),thickness=2)
        valor+=0.02
    
    if 13500 < area < 15000:
        print(contador)
        print("5 cêntimos")
        print(cv.contourArea(cont[contador]))
        cv.drawContours(teste,cont,contador,(0,0,255),thickness=2)
        cv.drawContours(imgcoins,cont,contador,(0,0,255),thickness=2)
        valor+=0.05
    if 12000 < area < 13500:
        print(contador)
        print("10 cêntimos")
        print(cv.contourArea(cont[contador]))
        cv.drawContours(teste,cont,contador,(0,0,255),thickness=2)
        cv.drawContours(imgcoins,cont,contador,(0,0,255),thickness=2)
        valor+=0.1

    if 15000 < area < 17500:
        print(contador)
        print("20 cêntimos")
        print(cv.contourArea(cont[contador]))
        cv.drawContours(teste,cont,contador,(0,0,255),thickness=2)
        cv.drawContours(imgcoins,cont,contador,(0,0,255),thickness=2)
        valor+=0.20

    if 19000 < area < 20000:
        print(contador)
        print("50 cêntimos")
        print(cv.contourArea(cont[contador]))
        cv.drawContours(teste,cont,contador,(0,0,255),thickness=2)
        cv.drawContours(imgcoins,cont,contador,(0,0,255),thickness=2)
        valor+=0.50
    if 17500 < area < 19000:
        print(contador)
        print("1 euro")
        print(cv.contourArea(cont[contador]))
        cv.drawContours(teste,cont,contador,(0,0,255),thickness=2)
        cv.drawContours(imgcoins,cont,contador,(0,0,255),thickness=2)
        valor+=1.0
    if 20000 < area < 22000:
        print(contador)
        print("2 euro")
        print(cv.contourArea(cont[contador]))
        cv.drawContours(teste,cont,contador,(0,0,255),thickness=2)
        cv.drawContours(imgcoins,cont,contador,(0,0,255),thickness=2)
        valor+=2.0
        


cv.putText(imgcoins,"Total= "+str(np.round(valor,2)),(100,100),cv.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

##            if 16000<cv.contourArea(cont[contador])<17000:
##                print(contador)
##                print("10 cêntimos")
##                print(cv.contourArea(cont[contador]))
##                cv.drawContours(teste,cont,contador,(0,0,255),thickness=2)
##                cv.drawContours(imgcoins,cont,contador,(0,0,255),thickness=2)            
##cv.drawContours(teste,cont,0,(0,0,255),thickness=2)

#cv2.drawContours(self.img, contourSeq, contorno, [0, 255, 0], thickness=2)
##cv.drawContours(teste,cont,26,(0,0,255),thickness=2)
##print(cv.contourArea(cont[26]))
cv.imshow('final',imgcoins)



cv.waitKey(0)
cv.destroyAllWindows()
