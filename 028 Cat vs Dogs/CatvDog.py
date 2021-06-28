#lynxdigital

import cv2
import numpy as np

capture = cv2.VideoCapture(0)
#capture = cv2.VideoCapture('303 (straightRoad).mp4')

dogDetector = cv2.CascadeClassifier("mydogdetector.xml")
catDetector = cv2.CascadeClassifier("mycatdetector2.xml")
faceDetector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

counter = 10
while True:

    isSuccessful, frame = capture.read()

    if isSuccessful: 

        grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        dog = dogDetector.detectMultiScale(grayFrame)
        cat = catDetector.detectMultiScale(grayFrame)
        #man = catDetector.detectMultiScale(grayFrame)

        frame = cv2.rectangle(frame, (20 + counter,20), (60, 60), (255, 255, 255), -1)
                
        for (x1,y1,w1,h1) in dog:
            if w1 > 400:
                grayFrame = cv2.rectangle(grayFrame, (x1,y1), (x1+w1, y1+h1), (255,0, 255), 2)
                cv2.putText(grayFrame, "This is a dog", (x1 + 5, y1 + 5), cv2.FONT_HERSHEY_DUPLEX, 0.5, (240,40,255), 1)
                print("Dog spotted!")
                
        for (x2,y2,w2,h2) in cat:
            if w2 > 400:
                grayFrame = cv2.rectangle(grayFrame, (x2,y2), (x2+w2, y2+h2), (255,0, 255), 2)
                cv2.putText(grayFrame, "This is a cat", (x2 + 5, y2 + 5), cv2.FONT_HERSHEY_DUPLEX, 0.5, (240,40,255), 1)
                print("Cat spotted!")    

        cv2.imshow("Frame", grayFrame)
    
    if cv2.waitKey(60) == ord('q'):
        break

        
capture.release()
cv2.destroyAllWindows()
