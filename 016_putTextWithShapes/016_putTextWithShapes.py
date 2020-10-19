'''
Reference: https://www.youtube.com/watch?v=43pCXboZ5hE

'''

import cv2
import numpy as np

capture = cv2.VideoCapture(0)
#capture = cv2.VideoCapture('001.mp4')

while True:

    isSuccessful, frame = capture.read()

    if isSuccessful:

        #for the rectangle
        startCoordinates = (100,100) #tuple of x and y coordinates of top left corner
        endCoordinates = (500,500) #tuple of x and y coordinates of bottom right corner
        colour = (0,255,0) #tuple for (B,G,R) colour
        thickness = 5
        startCoordinates
        #thickness = -1 means to colour the whole shape, positive integer refers to the shape line

        cv2.putText(frame, "This is a rectangle", (startCoordinates[0] + 5, startCoordinates[1] + 5), cv2.FONT_HERSHEY_DUPLEX, 0.5, (240,40,255), 1)
        cv2.putText(frame, "This is a rectangle", (startCoordinates[0] + 5, startCoordinates[1] + 100), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (240,40,255), 1)

        
        cv2.imshow("Frame", frame)
    
    if cv2.waitKey(60) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()

'''
FONT_HERSHEY_SIMPLEX = 0
FONT_HERSHEY_PLAIN = 1
FONT_HERSHEY_DUPLEX = 2
FONT_HERSHEY_COMPLEX = 3
FONT_HERSHEY_TRIPLEX = 4
FONT_HERSHEY_COMPLEX_SMALL = 5
FONT_HERSHEY_SCRIPT_SIMPLEX = 6
FONT_HERSHEY_SCRIPT_COMPLEX = 7
'''
