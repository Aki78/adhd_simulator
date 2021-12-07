import cv2
import numpy as np
import math
import ctypes
import os

gausslib = ctypes.CDLL('/home/aki/ADHDSimulator/gausslib.so')

# Read in image
image = cv2.imread('/home/aki/Pictures/adhd_text.png')

radius = 10
inputImage = image.copy() 
dist_radius2 = 4000
print(type(image))
outputImage =  image.copy()
print(image.shape)
inputImage_height = image.shape[1]
inputImage_width = image.shape[0]
print("width", inputImage_width)
X_CENTER = inputImage_width/2
Y_CENTER = inputImage_height/2
# We scale the sigma value in proportion to the radius
# Setting the minimum standard deviation as a baseline
sigma = max(radius / 2.0, 1)

# Enforces odd width kernel which ensures a center pixel is always available
kernelWidth = (2 * radius) + 1

# Initializing the 2D array for the kernel
kernel = np.zeros([kernelWidth, kernelWidth])
print("kernel type: ", kernel.dtype)
my_sum = 0.0

# Populate every position in the kernel with the respective Gaussian distribution value
# Remember that x and y represent how far we are away from the CENTER pixel
for x in range(-radius,radius ): 
    print(x)
    for y in range(-radius,radius ):
        exponentNumerator = -1.0*(x * x + y * y)
        # print("exponentNumerator", exponentNumerator)
        exponentDenominator = (2 * sigma * sigma)

        eExpression = math.exp(exponentNumerator / exponentDenominator)
        # print("sigma", sigma)
        # print("eExpression", eExpression)
        kernelValue = (eExpression / (2 * math.pi * sigma * sigma))

        # We add radius to the indices to prevent out of bound issues because x and y can be negative
        kernel[x + radius, y + radius] = kernelValue
        my_sum += kernelValue

# Normalize the kernel
# This ensures that all of the values in the kernel together add up to 1
for x in range(0, kernelWidth ):  # kernelWidth +1?
    for y in range(0, kernelWidth): # kernelWidth +1?
        kernel[x,y] /= my_sum

# Ignoring the edges for ease of implementation
# This will cause a thin border around the image that won't be processed
# os.mkdir('/home/aki/ImagesTest')
inputImage = inputImage.astype(int)
for x_v in range(40, 240):
    Y_CENTER = x_v
    outputImage = image.copy()
    outputImage = image.astype(int)
    inputImage = inputImage.astype(int)
    for x in range(radius, inputImage_width - radius ): # +1???
        # # print("X", x)
        # for y in range(radius ,inputImage_height - radius): # +1???
    # for x in range(1, inputImage_width ): # +1???
        # print("X", x)
        for y in range(radius ,inputImage_height -radius ): # +1???

            redValue = 0.0
            greenValue = 0.0
            blueValue = 0.0

            if ((x -  X_CENTER)*(x - X_CENTER) + (y - Y_CENTER)*(y - Y_CENTER) >dist_radius2 ):
                continue
            gausslib.compute_kernel(  ctypes.c_void_p(kernel.ctypes.data),  ctypes.c_void_p(inputImage.ctypes.data),  ctypes.c_void_p(outputImage.ctypes.data), ctypes.c_int(x), ctypes.c_int(y), ctypes.c_int(radius), ctypes.c_int(kernelWidth), ctypes.c_int(inputImage_width), ctypes.c_int(inputImage_height))
    print("saved", x_v)
    # print(outputImage)
    cv2.imwrite('Images/test' + "{:03d}".format(x_v) + '.jpg', outputImage)



# cv2.imshow('blur', blur)
cv2.imshow('outImg', outputImage)
cv2.imwrite('test.jpg', outputImage)
# cv2.imshow('image', image)
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread('opencv-logo-white.png')
blur = cv.blur(img,(5,5))
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()cv2.waitKey()
