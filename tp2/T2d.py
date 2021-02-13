import cv2 as cv2
import numpy as np

filePath = 'camera1.mov'
#cap = cv2.VideoCapture(filePath)


def processImages(frame1,frame2):

    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    median = cv2.medianBlur(gray, 3)
    blur = cv2.GaussianBlur(median, (5, 5), 0)

    #blur = cv2.GaussianBlur(gray, (9,9), 0)
    blur = cv2.medianBlur(gray, 3)
    _, thresh = cv2.threshold(blur, 25, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=20)

    return dilated


def readFrames(filePath):

    backgroundSub = cv2.createBackgroundSubtractorMOG2()
    cap = cv2.VideoCapture(filePath)
    
    if (cap.isOpened()== False):
        print("Error opening video stream or file")


    while cap.isOpened():

        ret,frame = cap.read()

        if ret == True:

           # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            median = cv2.medianBlur(frame, 3)
            blur = cv2.GaussianBlur(median, (5, 5), 0)

            backgroundMask = backgroundSub.apply(blur) # eliminar shadows

            threshold = cv2.threshold(backgroundMask, 200, 255, cv2.THRESH_BINARY)[1]
    
            opening = cv2.morphologyEx(threshold, cv2.MORPH_OPEN, np.ones((2, 2), np.uint8()), iterations = 1)
            closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, np.ones((2, 2), np.uint8()), iterations = 8)
            dilation = cv2.dilate(closing, np.ones((2, 2), np.uint8()))

            contoursImage = dilation.copy()
            cnts = cv2.findContours(contoursImage, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            contours, hierarchy = cnts

            for c in contours:
                x, y, w, h = cv2.boundingRect(c)
                (_x, _y), radius = cv2.minEnclosingCircle(c)
                center = (int(_x), int(_y))
                area = cv2.contourArea(c)

                if area > 250:
                    if area > 2000 and w > h:

                        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

                    elif area < 6000 and h > w:

                        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    
                elif area > 200:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                    
        cv2.imshow("feed", frame)
       


    

    cv2.destroyAllWindows()


readFrames(filePath)

                        




    



