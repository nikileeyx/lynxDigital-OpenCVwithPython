import cv2
import numpy as np

capture = cv2.VideoCapture(0)
#capture = cv2.VideoCapture('001.mp4')

faceReg = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:

    isSuccessful, frame = capture.read()

    if isSuccessful:

        grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = faceReg.detectMultiScale(grayFrame)

        for (x,y,w,h) in faces:
            frame = cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0, 255), 2)
            cv2.putText(frame, "This is a rectangle", (x + 5, y + 5), cv2.FONT_HERSHEY_DUPLEX, 0.5, (240,40,255), 1)

        
        cv2.imshow("Frame", frame)
    
    if cv2.waitKey(60) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
