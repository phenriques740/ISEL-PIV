import cv2 as cv2
import numpy as np
import collections


filePath = 'camera1.mov'
filePathDuarte = 'C:/Users/duart/OneDrive/Ambiente de Trabalho/ISEL/VIDEO/camera1.mov'



cap = cv2.VideoCapture(filePathDuarte)
ret, frame1 = cap.read()
ret, frame2 = cap.read()

backgroundSub = cv2.createBackgroundSubtractorMOG2(history = 500, varThreshold = 16, detectShadows = False)


def findBackground(frame2):
    
    
    
    gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

    blurm = cv2.medianBlur(gray, 3)
    blur = cv2.GaussianBlur(blurm,(5,5),0)
    diff = backgroundSub.apply(blur)
    _, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)
    
    #kernel = 
    
    #dilated = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, (22,22))
    
    #opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, np.ones((2, 2), np.uint8()), iterations = 1)
    #closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, np.ones((2, 2), np.uint8()), iterations = 8)
    #dilated = cv2.dilate(closing, np.ones((2, 2), np.uint8()))
    #erode = cv2.erode(thresh,None, iterations = 1)
    
    return diff, thresh



#FUNCAO PARA CLASSIFICAR
def classify(width,height):
    
    
    ratio = round(width / height,3)
    
    if((ratio) >= 1.10):
    
        return 0
                
                
    if((ratio) >= 0.40 and ratio <= 0.80):
     
        return 1
                
    if((ratio) > 0.80 and (ratio) < 1.10):
        
        return 2
    
    return None
        


def draw_rectangles(x,y,w,h,objClassified):
        
     if (objClassified==0):
         
    
         cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
         cv2.putText(frame1, str("Carro"),(x,y-10) , cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
    
     if (objClassified==1):
         
    
         cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 0, 255), 2)
         cv2.putText(frame1, str("Pessoa"),(x,y-10) , cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)    
                
        
     if (objClassified==2):
         
    
        cv2.rectangle(frame1, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(frame1, str("Outro"),(x,y-10) , cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)


                

def draw_lines(points,frame1):
    
    if(len(points)>0):
        
        for i in range (len (points)):
            
            if (points[i][0] ==0):
                
                cv2.circle(frame1,(points[i][1],points[i][2]),1,(0, 255, 0),1)
            if (points[i][0] ==1):
               
                cv2.circle(frame1,(points[i][1],points[i][2]),1,(0, 0, 255),1)
            if (points[i][0] ==2):
    
                cv2.circle(frame1,(points[i][1],points[i][2]),1,(255, 0, 0),1)
            
    
xd = collections.deque([])
try:
    ret, frame1 = cap.read()
    ret, frame2 = cap.read()

    #points =collections.deque([])
    

    
    if (cap.isOpened()== False):
        print("Error opening video stream or file")
        
    while cap.isOpened():
        
        
        
        if cv2.waitKey(5) == ord('q') or not ret:
            break
        
        diff,thresh = findBackground(frame2)
        
        
        #it = 5, no.ones(3,3)
        #opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, np.ones((2, 2), np.uint8()), iterations = 1)
        
        closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, np.ones((2, 2), np.uint8()), iterations = 5)
        dilate = cv2.dilate(closing, np.ones((3, 3), np.uint8()))
         
        contours, _ = cv2.findContours(dilate, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
         
        for contour in contours:
            
            draw_lines(xd,frame1)
            (x, y, w, h) = cv2.boundingRect(contour)
            
            if cv2.contourArea(contour) < 480:
                continue
            
            
            pos_x = int(x+w/2)
            pos_y = int(y+h/2)
            
            print (w/h)
            
            
            #RETORNA O TIPO DO OBJETO
            objClassified = classify(w,h)
            
            #DRAW STUFF
            draw_rectangles(x,y,w,h,objClassified)
       
        
           
            if objClassified ==0:
                
                xd.append((0,pos_x,pos_y))
                
            if objClassified ==1:
                
                xd.append((1,pos_x,pos_y))
                
            if objClassified ==2:
                
                xd.append((2,pos_x,pos_y))
            
           
        draw_lines(xd,frame1)
            
        image = cv2.resize(frame1, (1280,720))
        
        cv2.imshow("dilated" , dilate)
        cv2.imshow("feed", frame1)
         
        frame1 = frame2
         
        ret, frame2 = cap.read()
    
       
    cv2.destroyAllWindows()
    cap.release()
         
  
except Exception as e:
     print(e)
     cv2.destroyAllWindows()
     cap.release()




    



