import cv2
import scaledFrame

#capture = cv2.VideoCapture(0)
capture = cv2.VideoCapture("001.mp4")

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

        finalFrame = scaledFrame.scaleFrame(mergeFrame, scaledPercentage = 0.2)

        cv2.imshow("Blured Frame Compilation", finalFrame)

    else:
        break

    if cv2.waitKey(60) == ord('q'):
        break
    
capture.release()
cv2.destroyAllWindows()
