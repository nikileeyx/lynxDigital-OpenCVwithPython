'''
Created by LynxDigital
Please give credits for the code if used ^.^
YouTube: https://www.youtube.com/channel/UCJ7GIy9ArKLwxcLqw0j4e6w
Telegram: t.me/nikileeyyxx
______________________________
'''

import cv2

capture = cv2.VideoCapture(0)
#capture = cv2.VideoCapture("Road Clips/001.mp4")

while True:
    isSuccessful, frame = capture.read()

    if isSuccessful:

        grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        sobelFrameX = cv2.Sobel(grayFrame, cv2.CV_64F, 1, 0, ksize = 5)
        sobelFrameY = cv2.Sobel(grayFrame, cv2.CV_64F, 0, 1, ksize = 5)

        absGradientX = cv2.convertScaleAbs(sobelFrameX)
        absGradientY = cv2.convertScaleAbs(sobelFrameY)

        combinedXY = cv2.addWeighted(absGradientX, 0.5, absGradientY, 0.5, 0)

        cv2.imshow("Sobel Frame", combinedXY)
            
    else:
        break

    if cv2.waitKey(60) == ord('q'):
        break
    
capture.release()
cv2.destroyAllWindows()
