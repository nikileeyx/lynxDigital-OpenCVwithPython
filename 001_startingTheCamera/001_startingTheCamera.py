'''

Created by LynxDigital
Please give credits for the code if used ^.^

YouTube: https://www.youtube.com/channel/UCJ7GIy9ArKLwxcLqw0j4e6w
Telegram: t.me/nikileeyyxx
_______________________________
'''

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
