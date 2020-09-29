import cv2

capture = cv2.VideoCapture(0)
#capture = cv2.VideoCapture("Road Clips/001.mp4")

while True:
    isSuccessful, frame = capture.read()
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cannyFrame = cv2.Canny(frame, 100, 200)
    cannyFrameTwo = cv2.Canny(grayFrame, 100, 200)

    if isSuccessful:
        cv2.imshow("Canny Frame (CannyOne)", cannyFrame)
        cv2.imshow("Canny Frame (CannyTwo)", cannyFrameTwo)

    else:
        break

    if cv2.waitKey(60) == ord('q'):
        break
    
capture.release()
cv2.destroyAllWindows()
