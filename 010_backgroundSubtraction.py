'''
Created by LynxDigital
Please give credits for the code if used ^.^
YouTube: https://www.youtube.com/channel/UCJ7GIy9ArKLwxcLqw0j4e6w
Telegram: t.me/nikileeyyxx
______________________________
'''
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

#kernel = cv2.getStructuringElement(cv.MORPH_ELLIPSE, (3,3))
fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
#fgbg = cv2.bgsegm.BackgroundSubtractorGMG()
#fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=True)
#fgbg = cv2.createBackgroundSubtractorKNN(detectShadows=True)

while True:
    isSuccessful, frame = capture.read()

    if isSuccessful:
        
        fgmask = fgbg.apply(frame)
        #fgmask = cv.morphologyEx(fgmask, cv.MORPH_OPEN, kernel)

        percentScale = 0.3
        widthFrame = int(fgmask.shape[1] * percentScale)
        heightFrame = int(fgmask.shape[0] * percentScale)
        dimensionFrame = (widthFrame, heightFrame)
        scaledFrame = cv2.resize(fgmask, dimensionFrame, interpolation =cv2.INTER_AREA)
        
        cv2.imshow('Frame', scaledFrame)
        #cv2.imshow('FG MASK Frame', fgmask)
            
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
