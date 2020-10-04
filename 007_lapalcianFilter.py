'''
References:
Laplacian of Gaussian (LoG) - https://theailearner.com/tag/cv2-laplacian/
'''

import cv2

#capture = cv2.VideoCapture(0)
capture = cv2.VideoCapture("Road Clips/001.mp4")

while True:
    isSuccessful, frame = capture.read()

    if isSuccessful:
        grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blurFrame = cv2.GaussianBlur(grayFrame, (9,9), 0)

        laplaceFrame = cv2.Laplacian(blurFrame, cv2.CV_64F)

        percentScale = 0.4
        widthFrame = int(laplaceFrame.shape[1] * percentScale)
        heightFrame = int(laplaceFrame.shape[0] * percentScale)
        dqimensionFrame = (widthFrame, heightFrame)
        scaledFrame = cv2.resize(laplaceFrame, dimensionFrame, interpolation =cv2.INTER_AREA)

        percentScale = 0.4
        widthFrame = int(frame.shape[1] * percentScale)
        heightFrame = int(frame.shape[0] * percentScale)
        dimensionFrame = (widthFrame, heightFrame)
        scaledFrames = cv2.resize(frame, dimensionFrame, interpolation =cv2.INTER_AREA)

        cv2.imshow("Laplace Frame", scaledFrame)
        cv2.imshow("Original Frame", scaledFrames)

    else:
        break

    if cv2.waitKey(60) == ord('q'):
        break
    
capture.release()
cv2.destroyAllWindows()
