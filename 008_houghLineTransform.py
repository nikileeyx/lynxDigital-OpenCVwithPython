

import cv2
import numpy as np

capture = cv2.VideoCapture("Road Clips/001.mp4")

while True:
    isSuccessful, frame = capture.read()

    if isSuccessful:
        grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cannyFrame = cv2.Canny(grayFrame, 50, 200, 3)

        linesHough = cv2.HoughLines(cannyFrame, 1, np.pi / 180, 200)

        if linesHough is not None:
            for line in linesHough:
                #print(line)
                rho, theta = line[0]
                x = np.cos(theta)
                y = np.sin(theta)

                x0 = x * rho
                y0 = y * rho

                x1 = int(x0 + 1000 * (-y))
                y1 = int(y0 + 1000 * (x))

                x2 = int(x0 - 1000 * (-y))
                y2 = int(y0 - 1000 * (x))

                cv2.line(frame, (x1,y1), (x2,y2), (0,255,0), 4)

        percentScale = 0.4
        widthFrame = int(frame.shape[1] * percentScale)
        heightFrame = int(frame.shape[0] * percentScale)
        dimensionFrame = (widthFrame, heightFrame)
        scaledFrame = cv2.resize(frame, dimensionFrame, interpolation =cv2.INTER_AREA)

        cv2.imshow("Houghlines on Frame", scaledFrame)
        
    else:
        break

    if cv2.waitKey(60) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()

'''
References:
https://docs.opencv.org/3.4/d9/db0/tutorial_hough_lines.html
https://gist.github.com/pknowledge/62ad0d100d6d4df756c0374dee501131
https://numpy.org/doc/stable/reference/generated/numpy.copy.html

https://docs.opencv.org/master/d9/db0/tutorial_hough_lines.html
https://docs.opencv.org/master/d3/de6/tutorial_js_houghlines.html

https://gist.github.com/pknowledge/86a148c6cd5f0f2820ba81561cc00a8e
'''
