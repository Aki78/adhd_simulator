import cv2
import numpy as np
import math
import ctypes
import os


gausslib = ctypes.CDLL('/home/aki/ADHDSimulator/gausslib.so')
seconds_run = 10
seconds_osscilate = 5

def get_position(t):
    x = 200*math.sin(t/math.pi/ seconds_osscilate)
    return x, 400

# Read in image
for t in range(0, 24*seconds_run):
    X_CENTER, Y_CENTER = get_position(t)
    # image = cv2.imread('/home/aki/Pictures/adhd_text.png')
    inputImage =cv2.imread('Images/test' + "{:04d}".format(t) + '.jpg') 
    inputImage = inputImage.astype(int)
    inputImage2 =cv2.imread('full_006.jpg') 
    inputImage2 = inputImage2.astype(int)
    seconds_run = 10
    seconds_osscilate = 10
    dist_radius2 = 4000
    outputImage =  inputImage.copy()
    inputImage_height = inputImage.shape[1]
    inputImage_width = inputImage.shape[0]
    radius = 10

    for x in range(radius, inputImage_width - radius ): # +1???
        for y in range(radius ,inputImage_height -radius ): # +1???
            if ((x -  X_CENTER)*(x - X_CENTER) + (y - Y_CENTER)*(y - Y_CENTER) > dist_radius2):
                continue
            print(x,y)
            outputImage[x,y] = inputImage2[x,y]
    print("saved", t)
    cv2.imwrite('Images/test_final' + "{:04d}".format(t) + '.jpg', outputImage)
