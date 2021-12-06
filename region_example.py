import cv2

# Read in image
image = cv2.imread('/home/aki/Pictures/kantoMap.png')

# Create ROI coordinates
topLeft = (660, 440)
bottomRight = (1240, 650)
x, y = topLeft[0], topLeft[1]
w, h = bottomRight[0] - topLeft[0], bottomRight[1] - topLeft[1]

# Grab ROI with Numpy slicing and blur
ROI = image[y:y+h, x:x+w]
blur = cv2.GaussianBlur(ROI, (11,11), 2.5) 

# Insert ROI back into image
image[y:y+h, x:x+w] = blur

cv2.imshow('blur', blur)
cv2.imshow('image', image)
cv2.waitKey()
