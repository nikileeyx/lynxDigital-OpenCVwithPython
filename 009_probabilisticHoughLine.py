'''
Created by LynxDigital
Please give credits for the code if used ^.^
YouTube: https://www.youtube.com/channel/UCJ7GIy9ArKLwxcLqw0j4e6w
Telegram: t.me/nikileeyyxx
______________________________
'''

import cv2
import numpy as np

capture = cv2.VideoCapture("Road Clips/003 (NUS YIH).mp4")

while True:
    isSuccessful, frame = capture.read()

    if isSuccessful:
        grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cannyFrame = cv2.Canny(grayFrame, 150, 200, 5)

        houghLineP = cv2.HoughLinesP(cannyFrame, 1, np.pi / 180, 100, 100, 50)

        if houghLineP is not None:
            for theLines in houghLineP:
                x1, y1, x2, y2 = theLines[0]
                cv2.line(frame, (x1,y1), (x2,y2), (255,0,0), 2)
        
        percentScale = 0.3
        widthFrame = int(cannyFrame.shape[1] * percentScale)
        heightFrame = int(cannyFrame.shape[0] * percentScale)
        dimensionFrame = (widthFrame, heightFrame)
        scaledFrame = cv2.resize(cannyFrame, dimensionFrame, interpolation =cv2.INTER_AREA)
        
        cv2.imshow("Name", scaledFrame)
        
    else:
        break

    if cv2.waitKey(60) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
