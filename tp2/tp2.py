import math

import cv2 as cv2
import numpy as np
import pickle


video = cv2.VideoCapture('camera1.mov')
#capture frame by frame
ret, frame1 = video.read()
ret, frame2 = video.read()

objeto=""

local1=0
local2=0

#array_pessoa_area=[]
#array_pessoa_w=[]
#array_pessoa_h=[]
#array_pessoa_aspect_ratio=[]

#array_carro_area=[]
#array_carro_w=[]
#array_carro_h=[]
#array_carro_aspect_ratio=[]



while video.isOpened():


    dif = cv2.absdiff(frame1, frame2)

    gray = cv2.cvtColor(dif, cv2.COLOR_BGR2GRAY)

    #blur = cv2.GaussianBlur(gray, (5, 5), 0)
    median = cv2.medianBlur(gray, 3)

    _, tresh = cv2.threshold(median, 20, 255, cv2.THRESH_BINARY)

    dilated = cv2.dilate(tresh, None, iterations=9)

    #dilated = cv2.morphologyEx(tresh, cv2.MORPH_CLOSE, np.ones((1,1), np.uint8) )

    contoures, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)



    for contour in contoures:

        (x, y, w, h) = cv2.boundingRect(contour)

        if cv2.contourArea(contour) < 2500:
            continue
        if (w/h>1 or w/h<0.65):
            continue


        #array_pessoa_area.append(cv2.contourArea(contour))
        #array_pessoa_w.append(w)
        #array_pessoa_h.append(h)
        #array_pessoa_aspect_ratio.append(w/h)

        #array_carro_area.append(cv2.contourArea(contour))
        #array_carro_w.append(w)
        #array_carro_h.append(h)
        #array_carro_aspect_ratio.append(w/h)


        cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame1, "Status".format('Movement'), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
        #if (w<50):
        #    objeto="Pessoa"
        #elif(w>=100):
        #    objeto = "Carro"
        #else:
        #    objeto = "Outro"
        #w > h
        #if(w<h):
        #    objeto = "Pessoa"
        #elif( w > h):
        #    objeto = "Carro"
        #else:
        #    objeto = "Outro"


        #cv2.putText(frame1, objeto.format('Movement'), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255),2)




        #print("Width: ",w)
        #print("Height: ", h)
        print("area: ",cv2.contourArea(contour))
        print("aspect ratio: ",w/h)

    cv2.imshow("feed", frame1)
    cv2.imshow("bin", dilated)

    frame1 = frame2
    ret, frame2 = video.read()

    if cv2.waitKey(1) & 0xFF == ord('q') or ret==False:
        break

#PESSOA
#print("\n")
#print("area: ",array_pessoa_area[:20])
#print("w: ",array_pessoa_w[:20])
#print("h: ",array_pessoa_h[:20])
#print("w/h: ",array_pessoa_aspect_ratio[:20])

#dict={}
#dict["area"]=array_carro_area
#dict["w"]=array_carro_w
#dict["h"]=array_carro_h
#dict["w/h"]=array_carro_aspect_ratio

#dbfile = open('outro', 'wb')
#pickle.dump(dict, dbfile)
#dbfile.close()

cv2.destroyAllWindows()
video.release()

