'''
Created by LynxDigital
Please give credits for the code if used ^.^
YouTube: https://www.youtube.com/channel/UCJ7GIy9ArKLwxcLqw0j4e6w
Telegram: t.me/nikileeyyxx
______________________________
'''

import cv2
import numpy as np
import scaleFunction

capture = cv2.VideoCapture(0)
#capture = cv2.VideoCapture('303 (straightRoad).mp4')

faceReg = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eyeReg = cv2.CascadeClassifier("haarcascade_eye.xml")

counter = 10
while True:

    isSuccessful, frame = capture.read()

    if isSuccessful: 

        grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceReg.detectMultiScale(grayFrame)
        eye = eyeReg.detectMultiScale(grayFrame)
        frame = cv2.rectangle(frame, (20 + counter,20), (60, 60), (255, 255, 255), -1)

        for (x1,y1,w1,h1) in faces:
            frame = cv2.rectangle(frame, (x1,y1), (x1+w1, y1+h1), (255,0, 255), 2)
            cv2.putText(frame, "This is a face", (x1 + 5, y1 + 5), cv2.FONT_HERSHEY_DUPLEX, 0.5, (240,40,255), 1)
                    
                
            for (x2,y2,w2,h2) in eye:
                frame = cv2.rectangle(frame, (x2,y2), (x2+w2, y2+h2), (255,0, 255), 2)
                cv2.putText(frame, "Eye", (x2 + 5, y2 + 5), cv2.FONT_HERSHEY_DUPLEX, 0.5, (240,40,255), 1)

        frame = scaleFunction.rescale(frame, 50)
        cv2.imshow("Frame", frame)
    
    if cv2.waitKey(60) == ord('q'):
        break

        
capture.release()
cv2.destroyAllWindows()
