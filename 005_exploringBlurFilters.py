'''
Created by LynxDigital
Please give credits for the code if used ^.^ 
Feel free to reach out for collabs/assistance!

YouTube: https://www.youtube.com/channel/UCJ7GIy9ArKLwxcLqw0j4e6w
Telegram: t.me/nikileeyyxx

Episode 5 - Exploring Blur Filters
(1) Homogenous Blur
(2) Gaussian Blur
(3) Median Blur
(4) Bilaterial Filter
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
        medianBlur = cv2.medianBlur(grayFrame, 5)
        gaussBlur = cv2.GaussianBlur(grayFrame,  (25,25), 0)
        bilatBlur = cv2.bilateralFilter(grayFrame, 9, 75, 75)
        
        mergeFrame = cv2.hconcat([
            cv2.vconcat([blurFrame, medianBlur]),
            cv2.vconcat([gaussBlur, bilatBlur])
            ])
        
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
    
capture.release()
cv2.destroyAllWindows()
