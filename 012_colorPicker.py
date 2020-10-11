
'''
Created by LynxDigital
Please give credits for the code if used ^.^
YouTube: https://www.youtube.com/channel/UCJ7GIy9ArKLwxcLqw0j4e6w
Telegram: t.me/nikileeyyxx
______________________________
'''

import numpy as np
import cv2

def printIt(x):
    pass

capture = cv2.VideoCapture(0)

cv2.namedWindow("Trackbar")

cv2.createTrackbar("Blue", "Trackbar", 0 , 255 , printIt)
cv2.createTrackbar("Green", "Trackbar", 0 , 255 , printIt)
cv2.createTrackbar("Red", "Trackbar", 0 , 255 , printIt)


while True:
  
    isSuccesful, frame = capture.read() 
  
    if isSuccesful:

        blue = cv2.getTrackbarPos("Blue", "Trackbar")
        green = cv2.getTrackbarPos("Green", "Trackbar")
        red = cv2.getTrackbarPos("Red", "Trackbar")

        frame[:] = [blue, green, red]
        cv2.imshow("Frame", frame)
        
    else:
        break
        
    if cv2.waitKey(60) == ord('q'):
        break
    
capture.release()
cv2.destroyAllWindows()
