# -*- coding: utf-8 -*-

import numpy as np
import cv2 as cv
import collections

def detectMovement(t):
    vs = cv.VideoCapture('camera1.mov')
    capturing = True
    true, frame1 = vs.read()
    true, frame2 = vs.read()
    min_teste = 50
    deque=collections.deque([])
    while capturing:
        
        minAbsDiff = cv.absdiff(frame1,frame2)
        #cv.imshow("diff", minAbsDiff)
        gray = cv.cvtColor(minAbsDiff,cv.COLOR_BGR2GRAY)
        #cv.imshow("gray", gray)
        gray = cv.GaussianBlur(gray,(21,21),0)
        #cv.imshow("blur", gray)
        
        thresh = cv.threshold(gray,t,255,cv.THRESH_BINARY)[1]
        thresh = cv.dilate(thresh, None, iterations = 4)
        #cv.imshow("dilate", thresh)
        cnts, hierarchy = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        for contour in cnts:
            if cv.contourArea(contour) < 270:
                continue
            (x, y, w, h) = cv.boundingRect(contour)
            teste = round(w / h,3)
            deque.append(x)
            deque.append(y)
            ##print('w: ' , w)
            if((teste) >= 1.10):
                cv.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv.putText(frame1, str("Carro"),(x,y-10) , cv.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv.LINE_AA)
            if((teste) <= 0.70):
                cv.rectangle(frame1, (x, y), (x + w, y + h), (0, 0, 255), 2)
                cv.putText(frame1, str("Pessoa"),(x,y-10) , cv.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv.LINE_AA)    
                
            if((teste) < 1.10 and (teste) > 0.70):
                if teste < min_teste:
                    min_teste = teste
                cv.rectangle(frame1, (x, y), (x + w, y + h), (255, 0, 0), 2)
                cv.putText(frame1, str("Outro"),(x,y-10) , cv.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv.LINE_AA)
            if(len(deque)>0):
                a=len(deque)
                b=0
                while b<a:
                    cv.circle(frame1,(deque[b],deque[b+1]),1,(0,255,255),5)
                    b+=2

        cv.imshow("Detecao de Movimento", frame1)

        key = cv.waitKey(1) & 0xFF
            
        if key == ord("q"):
            capturing = False
        frame1 = frame2
        vs.read()
        vs.read()
        true, frame2 = vs.read()
        if not true:
            break
    vs.release()
    cv.destroyAllWindows()
    
vs = None    
detectMovement(15)

