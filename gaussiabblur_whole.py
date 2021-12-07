import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread('/home/aki/Pictures/adhd_text.png')
for i in range(1, 20):
    blur = cv.blur(img,(i,2*i))
    cv.imwrite('full_' + "{:03d}".format(i)  + '.jpg', blur)
# plt.subplot(121),plt.imshow(img),plt.title('Original')
# plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
# plt.xticks([]), plt.yticks([])
# plt.show()
