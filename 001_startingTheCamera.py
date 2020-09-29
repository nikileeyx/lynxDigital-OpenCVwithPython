import cv2

#capture = cv2.VideoCapture(0)
capture = cv2.VideoCapture("Road Clips/001.mp4")

while True:
    isSuccessful, frame = capture.read()
    print(isSuccessful)

    if isSuccessful:
        cv2.imshow("Frame", frame)

    else:
        break

    if cv2.waitKey(60) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
