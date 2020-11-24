'''
Created by LynxDigital
Please give credits for the code if used ^.^
YouTube: https://www.youtube.com/channel/UCJ7GIy9ArKLwxcLqw0j4e6w
Telegram: t.me/nikileeyyxx
______________________________
'''

import numpy as np
import cv2

capture = cv2.VideoCapture(0)
  
while True: 
  
    isSuccesful, frame = capture.read() 
  
    if isSuccesful:

        blue = frame[ : , : , :1]
        green = frame[ : , : , 1:2]
        red = frame[ : , : , 2:]
        #print(red[2])

        blueMean = np.mean(blue)
        greenMean = np.mean(green)
        redMean = np.mean(red)

        if (blueMean > greenMean and blueMean > redMean):
            print("This frame is predominantly blue!")

        elif (greenMean > blueMean and greenMean > redMean):
            print("This frame is predominantly green!")

        elif (redMean > blueMean and redMean > greenMean):
            print("This frame is predominantly red!")
            
        elif (greenMean and blueMean and redMean < 30):
            print("This frame is predominantly dark!")

    else:
        break
    
    cv2.imshow("Frame", frame)
    
    if cv2.waitKey(60) == ord('q'):
        break
    
capture.release()
cv2.destroyAllWindows()

'''
References
https://www.geeksforgeeks.org/detect-the-rgb-color-from-a-webcam-using-python-opencv/
importing required libraries 
'''
