'''
Created by LynxDigital
Please give credits for the code if used ^.^ 
Feel free to reach out for collabs/assistance!

YouTube: https://www.youtube.com/channel/UCJ7GIy9ArKLwxcLqw0j4e6w
Telegram: t.me/nikileeyyxx

Episode 4 - Introduction to Blurring Filters
(1) Homogenous Blur
(2) Varying of Kernel Size
______________________________
'''

import cv2

#capture = cv2.VideoCapture(0)
capture = cv2.VideoCapture("Road Clips/001.mp4")

while True:
    isSuccessful, frame = capture.read()

    if isSuccessful:
        grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        blurFrame = cv2.blur(grayFrame, (25,25))

        mergeFrame = cv2.vconcat([grayFrame, blurFrame])
        
        percentScale = 0.2
        widthFrame = int(mergeFrame.shape[1] * percentScale)
        heightFrame = int(mergeFrame.shape[0] * percentScale)
        dimensionFrame = (widthFrame, heightFrame)
        scaledFrame = cv2.resize(mergeFrame, dimensionFrame, interpolation =cv2.INTER_AREA)

        cv2.imshow("Blured Frame Compilation", scaledFrame)

    else:
        break

    if cv2.waitKey(60) == ord('q'):
        break
    
#Default code
capture.release()
cv2.destroyAllWindows()
