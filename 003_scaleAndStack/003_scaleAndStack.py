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
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cannyFrame = cv2.Canny(frame, 50, 200)
    cannyFrameTwo = cv2.Canny(grayFrame, 100, 200)
    cannyFrameThree = cv2.Canny(grayFrame, 150, 200)

    mergeFrame = cv2.hconcat([
        cv2.vconcat([cannyFrame, cannyFrameThree]),
        cv2.vconcat([cannyFrame, grayFrame])
        ])

    percentScale = 0.2
    widthFrame = int(mergeFrame.shape[1] * percentScale)
    heightFrame = int(mergeFrame.shape[0] * percentScale)
    dimensionFrame = (widthFrame, heightFrame)
    scaledFrame = cv2.resize(mergeFrame, dimensionFrame, interpolation =cv2.INTER_AREA)
    
    if isSuccessful:
        cv2.imshow("Canny Frame (Color)", scaledFrame)
        #cv2.imshow("Canny Frame (Grayscale)", grayFrame)

    else:
        break

    if cv2.waitKey(60) == ord('q'):
        break
    
capture.release()
cv2.destroyAllWindows()
