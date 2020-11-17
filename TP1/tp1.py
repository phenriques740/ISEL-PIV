import numpy as np
import cv2
import glob
fileDir = "ImageDatabase/"
LENGTH_IMGS = 9
#fileName = "lily-lotus-flowers.jpg"
titles = [f"image {i}"for i in range (9)]
images = [cv2.imread(file) for file in glob.glob("TP1\PIV_20_21_TL1_imagens_treino/*.jpg")]
imagesGrey = [cv2.cvtColor(i,cv2.COLOR_BGR2GRAY) for i in images]
imagesBin = [cv2.threshold(i,127,255,cv2.THRESH_OTSU)[0] for i in imagesGrey]
thresh = [cv2.threshold(i,127,255,cv2.THRESH_OTSU)[1] for i in imagesGrey]
contours = [ cv2.findContours(i, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0] for i in thresh]
hierarchy  = [ cv2.findContours(i, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[1] for i in thresh]
#areas = [cv2.contourArea(i) for j in i in contours]
#x = cv2.boundingRect()

#rect = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),1)

#kernel 
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
#kernel = np.ones((2,2),np.uint8)

#dilation
imgsDilated = [cv2.dilate(i,kernel,iterations = 1) for i in imagesBin]


def show(arr):
    for i in range (LENGTH_IMGS):
        cv2.imshow(titles[i],arr[i])

def drawComponents(imgs,countours):
    for i in range (LENGTH_IMGS):
        cv2.drawContours(imgs[i], contours[i], -1, (0,255,0), 3)


drawComponents(thresh,contours)
show(thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()

