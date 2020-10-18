import cv2
import numpy as np

#capture = cv2.VideoCapture(0)
capture = cv2.VideoCapture('001.mp4')

while True:

    isSuccessful, frame = capture.read()

    if isSuccessful:

        #for the rectangle
        startCoordinates = (10,10) #tuple of x and y coordinates of top left corner
        endCoordinates = (50,50) #tuple of x and y coordinates of bottom right corner
        colour = (0,255,0) #tuple for (B,G,R) colour
        thickness = -1
        #thickness = -1 means to colour the whole shape, positive integer refers to the shape line
        
        rectangle = cv2.rectangle(frame, startCoordinates, endCoordinates, colour, thickness)
        
        #for the circle
        centre = (500,500) #tuple of x and y coordinates
        radius = 50 #measured in pixels
       
        circle = cv2.circle(frame, centre, radius, colour, thickness)
        
        
        cv2.imshow("Frame", frame)
    
    if cv2.waitKey(60) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
