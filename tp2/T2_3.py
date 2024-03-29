import cv2
import numpy as np

filePath = 'camera1.mov'

cap = cv2.VideoCapture(filePath)
ret, frame1 = cap.read()
ret, frame2 = cap.read()

def processImages(frame1,frame2):

    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    median = cv2.medianBlur(gray, 3)
    blur = cv2.GaussianBlur(median, (5, 5), 0)

    #blur = cv2.GaussianBlur(gray, (9,9), 0)
    _, thresh = cv2.threshold(blur, 25, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=20)

    return dilated




try:
    ret, frame1 = cap.read()
    ret, frame2 = cap.read()

    
    if (cap.isOpened()== False):
        print("Error opening video stream or file")

    while cap.isOpened():

         dilate = processImages(frame1,frame2)
         
         contours, _ = cv2.findContours(dilate, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
         
         for contour in contours:
             
            (x, y, w, h) = cv2.boundingRect(contour)
    
            if cv2.contourArea(contour) < 900:
                continue
            cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame1, "Status: {}".format('Movement'), (10, 20), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0, 0, 255), 3)
        
        
         image = cv2.resize(frame1, (1280,720))
        
         cv2.imshow("dilated" , dilate)
         cv2.imshow("feed", frame1)
         
         frame1 = frame2
         
         ret, frame2 = cap.read()
    
         if cv2.waitKey(40) == ord('q') or not ret:
            break
    cv2.destroyAllWindows()
    cap.release()
         
  
except Exception as e:
     print(e)
     cv2.destroyAllWindows()
     cap.release()


class VideoMovementTracker:
    def __init__(self, videoPath):
        self.path = videoPath
        self.capture = cv2.VideoCapture(self.path)
        
        if not self.capture.isOpened():
            print('Unable to open: ' + videoPath)
            return            
        return 
    
    
    def findBackground(f1, f2):
        diff = cv2.absdiff(frame1, frame2)
        gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    
        median = cv2.medianBlur(gray, 3)
        blur = cv2.GaussianBlur(median, (5, 5), 0)
    
        #blur = cv2.GaussianBlur(gray, (9,9), 0)
        _, thresh = cv2.threshold(blur, 25, 255, cv2.THRESH_BINARY)
        dilated = cv2.dilate(thresh, None, iterations=20)        
    

    



