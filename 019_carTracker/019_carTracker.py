import cv2
import numpy as np
import scaleFunction

#capture = cv2.VideoCapture(0)
capture = cv2.VideoCapture('Pedestrians Compilation.mp4')

carDetect = cv2.CascadeClassifier("car_detector.xml")
    
while True:

    isSuccessful, frame = capture.read()

    if isSuccessful:

        grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        carSpotted = carDetect. detectMultiScale(grayFrame)

        for (x1,y1,w,h) in carSpotted:
            print(carSpotted)
            if w > 50 and h > 50:
                frame = cv2.rectangle(frame, (x1,y1), (x1+w, y1+h), (255, 0, 255), 1)
                cv2.putText(frame, "Car is Spotted!", (x1,y1), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0,0,0), 1)

        #frame = scaleFunction.rescale(frame, 30)
        cv2.imshow("Frame", frame)
        
    if cv2.waitKey(60) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
