'''
Created by LynxDigital
Please give credits for the code if used ^.^
YouTube: https://www.youtube.com/channel/UCJ7GIy9ArKLwxcLqw0j4e6w
Telegram: t.me/nikileeyyxx
______________________________
'''

import numpy as np
import cv2


capture = cv2.VideoCapture("Road Clips/003 (NUS YIH).mp4")
#insert the path to your own video here! 
#capture = cv2.VideoCapture(0) #uncomment this line for your device's camera

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
foreBack = cv2.bgsegm.createBackgroundSubtractorMOG()

while True:
    isSuccessful, frame = capture.read()

    if isSuccessful:

        foregroundMask = foreBack.apply(frame)
        morphMask = cv2.morphologyEx(foregroundMask, cv2.MORPH_OPEN, kernel)
        
        percentScale = 0.3
        widthFrame = int(morphMask.shape[1] * percentScale)
        heightFrame = int(morphMask.shape[0] * percentScale)
        dimensionFrame = (widthFrame, heightFrame)
        scaledFrame = cv2.resize(morphMask, dimensionFrame, interpolation =cv2.INTER_AREA)

        percentScale = 0.3
        widthFrame = int(foregroundMask.shape[1] * percentScale)
        heightFrame = int(foregroundMask.shape[0] * percentScale)
        dimensionFrame = (widthFrame, heightFrame)
        scaledFrame2 = cv2.resize(foregroundMask, dimensionFrame, interpolation =cv2.INTER_AREA)
                
        cv2.imshow('Morph', scaledFrame)
        cv2.imshow('Foreground', scaledFrame2)

        
    else:
        break

    if cv2.waitKey(60) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()

'''
References
https://docs.opencv.org/master/de/de1/group__video__motion.html
https://www.youtube.com/watch?v=eZ2kDurOodI
'''
