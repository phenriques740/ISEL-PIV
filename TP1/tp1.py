import numpy as np
import cv2
import glob
fileDir = "PIV_20_21_TL1_imagens_treino/"
LENGTH_IMGS = 9
#fileName = "lily-lotus-flowers.jpg"
titles = [f"image {i}"for i in range (9)]
images = [cv2.imread(file) for file in glob.glob("PIV_20_21_TL1_imagens_treino/*.jpg")]
imagesGrey = [cv2.cvtColor(i,cv2.COLOR_BGR2GRAY) for i in images] #images greyscale
imagesBin , thresh = zip(*[cv2.threshold(i,127,255,cv2.THRESH_OTSU) for i in imagesGrey])

contours, hierarchy = zip(*[cv2.findContours(i, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) for i in thresh]) #contours

#kernel matriz 3x3 rectangular
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
#kernel = np.ones((2,2),np.uint8)

#dilation
imgsDilated = [cv2.dilate(i,kernel,iterations = 1) for i in imagesBin]


def getContour(cnt): #guarda as bounding boxes duma images num array
    bbArr=[]
    for i in cnt:
        area =  cv2.contourArea(i)
        if area > 15:
            BB = cv2.boundingRect(i)
            bbArr.append(BB)
    return bbArr

def getAllContours(cnts): #guarda as bounding boxes de todas as imagens num array

    cntsArr = []

    for i in cnts:
        cntsArr.append(getContour(i))
    return cntsArr


def drawRectangle(bb,img): #faz os rectangulos para uma imagem
    for i in range (len(bb)):
        x = bb[i][0]
        y =bb[i][1]
        w = bb[i][2]
        h= bb[i][3]
       
        cv2.rectangle(img,(x,y),(x+w,y+h),(255, 0, 0) ,1)

def drawAllRectangles(bbx,img): #faz os rectangulos para todas as imagens
    
    for i in range (len(bbx)):
        drawRectangle(bbx[i],img[i])
  

def show(arr): #show das imagens
    for i in range (LENGTH_IMGS):
        cv2.imshow(titles[i],arr[i])

def drawContours(imgs,countours): #draw dos countours
    for i in range (LENGTH_IMGS):
        cv2.drawContours(imgs[i], contours[i], -1, (0,255,0), 3)

bbx = getAllContours(contours) #bounding boxes 
drawAllRectangles(bbx,thresh) #draw dos rectangulos para todas as imagens
#drawContours(thresh,contours) DESCOMENTA ISTO SE QUISERES PARA TESTARES 
#drawContours(thresh,contours)
#drawRectangle(boundingBoxes,thresh[0])
#drawContours(thresh,contours)
show(imagesGrey)
cv2.waitKey(0)
cv2.destroyAllWindows()

