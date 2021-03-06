'''

LYNXDigital OpenCV Series
It ranges from 0 to 255, with 0 being completely dark and 255 being fully bright. 
White has an HSV value of 0-255, 0-255, 255. 
Black has an HSV value of 0-255, 0-255, 0. 
The dominant description for black and white is the term, value.

'''

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:

    isSuccessful, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of yellow color in HSV
    lower_yellow = np.array([204,204,0])
    upper_yellow = np.array([255,255,254])

    # Threshold the HSV image to get only yellow colors
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(60) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()

    isSuccessful, frame = cap.read()
    isSuccessful, frame = cap.read()
