#LynxDigital Car Lane and Vehicle Detection

import matplotlib.pylab as plt1qq
import cv2
import numpy as np

def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    #channel_count = img.shape[2]
    match_mask_color = 255
    cv2.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image

def drow_the_lines(img, lines):
    img = np.copy(img)
    blank_image = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)

    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(blank_image, (x1,y1), (x2,y2), (0, 255, 0), thickness=10)

    img = cv2.addWeighted(img, 0.8, blank_image, 1, 0.0)
    return img

# = cv2.imread('road.jpg')
#image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
def process(image):
    print(image.shape)
    height = image.shape[0]
    width = image.shape[1]
    region_of_interest_vertices = [
        (0, height),
        (width/2, height/2),
        (width, height)
    ]
    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    canny_image = cv2.Canny(gray_image, 100, 120)
    cropped_image = region_of_interest(canny_image,
                    np.array([region_of_interest_vertices], np.int32),)
    lines = cv2.HoughLinesP(cropped_image,
                            rho=2,
                            theta=np.pi/180,
                            threshold=50,
                            lines=np.array([]),
                            minLineLength=40,
                            maxLineGap=100)
    image_with_lines = drow_the_lines(image, lines)
    return image_with_lines

captureVideo = cv2.VideoCapture('102 (Highway).mp4')
car_detector = cv2.CascadeClassifier("car_detector.xml")

#captureVideo = cv2.

while captureVideo.isOpened():
    ret, frame = captureVideo.read()

    percentScale = 0.4
    widthFrame = int(frame.shape[1] * percentScale)
    heightFrame = int(frame.shape[0] * percentScale)
    dimensionFrame = (widthFrame, heightFrame)
    frame = cv2.resize(frame, dimensionFrame, interpolation =cv2.INTER_AREA)
    
    frame = process(frame)

    carSpotted = car_detector.detectMultiScale(frame)

    for (x1,y1,w,h) in carSpotted:
        print(carSpotted)
        if w > 50 and h > 50:
            frame = cv2.rectangle(frame, (x1,y1), (x1+w, y1+h), (255, 0, 255), 1)
            cv2.putText(frame, "Car is Spotted!", (x1,y1), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0,0,0), 1)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
