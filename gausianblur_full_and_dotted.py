import cv2
import numpy as np
import math

# Read in image
image0 = cv2.imread('/home/aki/ADHDSimulator/full_000.jpg')
image1 = cv2.imread('/home/aki/ADHDSimulator/full_001.jpg')
image2 = cv2.imread('/home/aki/ADHDSimulator/full_002.jpg')
image3 = cv2.imread('/home/aki/ADHDSimulator/full_003.jpg')
image4 = cv2.imread('/home/aki/ADHDSimulator/full_004.jpg')
image5 = cv2.imread('/home/aki/ADHDSimulator/full_005.jpg')
image6 = cv2.imread('/home/aki/ADHDSimulator/full_006.jpg')

def gauss_distribution(x, mu, tau):
    return math.sqrt(tau/2/math.pi)*math.exp(-tau*(x - mu)**2/2)

def get_dist_array(distribution, n, mu, tau):
    ys = np.zeros(n)
    for k in range(0,n):
       ys[k] = distribution(1.0*k, mu, tau) 

    return ys

print(get_dist_array(gauss_distribution,6, 2, 1.5 ))

imageOut = cv2.imread('/home/aki/ADHDSimulator/full_000.jpg')
w = image0.shape[0]
h = image0.shape[1]
w = 1.0 * np.arange(20)
w =np.exp(np.array([0,1,2,3,4,5,6.0])**2)
seconds_blur = 5
seconds_run = 10
for t in range(0, 24*seconds_run):
    x = abs(10*math.sin(t/24/seconds_blur*math.pi))
    shiftX = 5
    w = get_dist_array(gauss_distribution,6, x - shiftX, 1.5 )
    imageOut =  w[0]*image0 + w[1]*image1 + w[2]*image2 + w[3]*image3 + w[4]*image4 + w[5]*image5 
    imageOut /= np.sum(w)
    cv2.imwrite('Images/test' + "{:04d}".format(t) + '.jpg', imageOut)
