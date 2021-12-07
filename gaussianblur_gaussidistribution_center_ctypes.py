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
    seconds_run = 10
    seconds_osscilate = 10

    radius = 10
    # inputImage = image.copy() 
    dist_radius2 = 4000
    outputImage =  inputImage.copy()
    inputImage_height = inputImage.shape[1]
    inputImage_width = inputImage.shape[0]
    print("width", inputImage_width)
    sigma = max(radius / 2.0, 1)

    kernelWidth = (2 * radius) + 1

    kernel = np.zeros([kernelWidth, kernelWidth])
    print("kernel type: ", kernel.dtype)
    my_sum = 0.0

    for x in range(-radius,radius ): 
        print(x)
        for y in range(-radius,radius ):
            exponentNumerator = -1.0*(x * x + y * y)
            exponentDenominator = (2 * sigma * sigma)

            eExpression = math.exp(exponentNumerator / exponentDenominator)
            kernelValue = (eExpression / (2 * math.pi * sigma * sigma))

            kernel[x + radius, y + radius] = kernelValue
            my_sum += kernelValue

    for x in range(0, kernelWidth ):  # kernelWidth +1?
        for y in range(0, kernelWidth): # kernelWidth +1?
            kernel[x,y] /= my_sum



    for x in range(radius, inputImage_width - radius ): # +1???
        for y in range(radius ,inputImage_height -radius ): # +1???

            redValue = 0.0
            greenValue = 0.0
            blueValue = 0.0

            if ((x -  X_CENTER)*(x - X_CENTER) + (y - Y_CENTER)*(y - Y_CENTER) >dist_radius2 ):
                continue
            gausslib.compute_kernel(  ctypes.c_void_p(kernel.ctypes.data),  ctypes.c_void_p(inputImage.ctypes.data),  ctypes.c_void_p(outputImage.ctypes.data), ctypes.c_int(x), ctypes.c_int(y), ctypes.c_int(radius), ctypes.c_int(kernelWidth), ctypes.c_int(inputImage_width), ctypes.c_int(inputImage_height))
    print("saved", t)
    cv2.imwrite('Images/test_final' + "{:04d}".format(t) + '.jpg', outputImage)



cv2.imshow('outImg', outputImage)
cv2.imwrite('test.jpg', outputImage)
