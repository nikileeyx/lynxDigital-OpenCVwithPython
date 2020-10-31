'''
LynxDigital YouTube Channel:
This code alone will not execute any file, this is a file with functions that will be used by the main program.
'''

import cv2
import numpy as np

#Scaling Frame Function that takes two arguements, 
#one is the frame and the second is the scaled frame as a percentage.
#you can set "scaledPercentage = 50" if you want a frame

def scaleFrame(frame, scaledPercentage):
    percentScale = scaledPercentage
    widthFrame = int(frame.shape[1] * percentScale)
    heightFrame = int(frame.shape[0] * percentScale)
    dimensionFrame = (widthFrame, heightFrame)
    scaledFrame = cv2.resize(frame, dimensionFrame, interpolation =cv2.INTER_AREA)
    return scaledFrame
