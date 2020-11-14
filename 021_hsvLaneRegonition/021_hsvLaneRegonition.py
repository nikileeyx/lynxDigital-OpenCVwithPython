import cv2
import numpy as np

camera = cv2.VideoCapture("das.mp4")

def nothing(x):
    pass

def scaleFrame(frame, scaledPercentage):
    percentScale = scaledPercentage
    widthFrame = int(frame.shape[1] * percentScale)
    heightFrame = int(frame.shape[0] * percentScale)
    dimensionFrame = (widthFrame, heightFrame)
    scaledFrame = cv2.resize(frame, dimensionFrame, interpolation =cv2.INTER_AREA)
    return scaledFrame

cv2.namedWindow('marking')

cv2.createTrackbar('H Lower','marking',0,179,nothing)
cv2.createTrackbar('H Higher','marking',179,179,nothing)
cv2.createTrackbar('S Lower','marking',0,255,nothing)
cv2.createTrackbar('S Higher','marking',255,255,nothing)
cv2.createTrackbar('V Lower','marking',0,255,nothing)
cv2.createTrackbar('V Higher','marking',255,255,nothing)


while(1):
    _,img = camera.read()
    if _:
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        hL = cv2.getTrackbarPos('H Lower','marking')
        hH = cv2.getTrackbarPos('H Higher','marking')
        sL = cv2.getTrackbarPos('S Lower','marking')
        sH = cv2.getTrackbarPos('S Higher','marking')
        vL = cv2.getTrackbarPos('V Lower','marking')
        vH = cv2.getTrackbarPos('V Higher','marking')

        LowerRegion = np.array([hL,sL,vL],np.uint8)
        upperRegion = np.array([hH,sH,vH],np.uint8)

        redObject = cv2.inRange(hsv,LowerRegion,upperRegion)

        kernal = np.ones((1,1),"uint8")

        red = cv2.morphologyEx(redObject,cv2.MORPH_OPEN,kernal)
        red = cv2.dilate(red,kernal,iterations=1)

        res1=cv2.bitwise_and(img, img, mask = red)
        res2 = scaleFrame(res1, 0.4)
        img2 = scaleFrame(img, 0.4)


        cv2.imshow("Masking",res2)
        cv2.imshow("Original",img2)
    else:
        break
