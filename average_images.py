import cv2
import numpy as np
import math
import os
import sys

# Read in image
image1 = cv2.imread(sys.argv[1])
image2 = cv2.imread(sys.argv[2])

outputImage = image1/2 + image2/2
cv2.imwrite('test.jpg', outputImage)
