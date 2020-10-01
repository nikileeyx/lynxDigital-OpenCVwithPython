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
    
capture.release()
cv2.destroyAllWindows()
