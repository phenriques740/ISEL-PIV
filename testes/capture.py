# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 20:39:56 2020

@author: pedro

Teste para abrir e capturar imagens com webcam usando OpenCV2
"""

import cv2, time

video = cv2.VideoCapture(0)

a = 0

while True:
    a = a+1
    
    check, frame = video.read()
    
    
    if(check):
        #se imagem existe, mostrar
        cv2.imshow("capture", frame)
        key = cv2.waitKey(1)
        
        if key == ord('q'):
            break

video.release()
cv2.destroyAllWindows()