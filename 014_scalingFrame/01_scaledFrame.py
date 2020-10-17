import cv2
import numpy as np

def scaleFrame(frame, scaledPercentage):
    percentScale = scaledPercentage
    widthFrame = int(frame.shape[1] * percentScale)
    heightFrame = int(frame.shape[0] * percentScale)
    dimensionFrame = (widthFrame, heightFrame)
    scaledFrame = cv2.resize(frame, dimensionFrame, interpolation =cv2.INTER_AREA)
    return scaledFrame
