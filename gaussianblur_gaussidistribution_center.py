import cv2
import numpy as np
import math

# Read in image
image = cv2.imread('/home/aki/Pictures/adhd_text.png')

# # Create ROI coordinates
# topLeft = (660, 440)
# bottomRight = (1240, 650)
# x, y = topLeft[0], topLeft[1]
# w, h = bottomRight[0] - topLeft[0], bottomRight[1] - topLeft[1]

# # Grab ROI with Numpy slicing and blur
# ROI = image[y:y+h, x:x+w]
# blur = cv2.GaussianBlur(ROI, (11,11), 2.5) 

# # Insert ROI back into image
# image[y:y+h, x:x+w] = blur
# print(np.exp(0.01*np.sum(image[30,30]        )))

# Returns a gaussian blurred image
# - Parameters:
#  The kernel will be 1 + (2 * radius) in width/height to ensure center pixel exists.
radius = 4
inputImage = image.copy() 
dist_radius2 = 4000
print(type(image))
outputImage =  image.copy()
print(image.shape)
inputImage_height = image.shape[1]
inputImage_width = image.shape[0]
print("height:", inputImage_height)
print("width:", inputImage_width)
X_CENTER = inputImage_width/2
Y_CENTER = inputImage_height/2
# We scale the sigma value in proportion to the radius
# Setting the minimum standard deviation as a baseline
sigma = max(radius / 2.0, 1)

# Enforces odd width kernel which ensures a center pixel is always available
kernelWidth = (2 * radius) + 1

# Initializing the 2D array for the kernel
kernel = np.zeros([kernelWidth, kernelWidth])
print("kernel type", kernel.dtype)
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
    print(x)
    for y in range(0, kernelWidth): # kernelWidth +1?
        kernel[x,y] /= my_sum

# Ignoring the edges for ease of implementation
# This will cause a thin border around the image that won't be processed
# os.mkdir('/home/aki/ImagesTest')
inputImage = inputImage.astype(int)
for x_v in range(0, 240):
    Y_CENTER = x_v
    outputImage = image.copy()
    outputImage = outputImage.astype(int)
    inputImage = outputImage.astype(int)
    for x in range(radius, inputImage_width - radius ): # +1???
        print(x)
        for y in range(radius, inputImage_height - radius): # +1???

            redValue = 0.0
            greenValue = 0.0
            blueValue = 0.0

            # This is the convolution step
            # We run the kernel over this grouping of pixels centered around the pixel at (x,y)
            if ((x -  X_CENTER)*(x - X_CENTER) + (y - Y_CENTER)*(y - Y_CENTER) >dist_radius2 ):
                continue
            for kernelX in range(-radius,radius): # +1?
                for kernelY in range(-radius, radius):

                    # Load the weight for this pixel from the convolution matrix
                    kernelValue = kernel[kernelX + radius, kernelY + radius]

                    # Multiply each channel by the weight of the pixel as specified by the kernel
                    # print(kernelValue)
                    # print(x,y,kernelValue)
                    redValue += inputImage[x - kernelX, y - kernelY, 0] * kernelValue # change .red etc
                    greenValue += inputImage[x - kernelX, y - kernelY, 1] * kernelValue
                    blueValue += inputImage[x - kernelX, y - kernelY, 2] * kernelValue

            # New RGB value for output image at position (x,y)
            #outputImage[x,y].red = UInt8(redValue)
            outputImage[x,y,0] = redValue
            outputImage[x,y,1] = greenValue
            outputImage[x,y,2] = blueValue
    print("saved", x_v)
    cv2.imwrite('Images/test' + "{:03d}".format(x_v) + '.jpg', outputImage)



# cv2.imshow('blur', blur)
cv2.imshow('outImg', outputImage)
cv2.imwrite('test.jpg', outputImage)
# cv2.imshow('image', image)
cv2.waitKey()
