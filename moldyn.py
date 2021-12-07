import numpy as np
from PIL import Image
import math
import matplotlib.pyplot as plt
import random

boxSize = 100

def force(a ,X):
    r = X[0]*X[0] + X[1]*X[1]
    # return [-X[0]*a/math.sqrt(r)**3 + 0.001*X[0]*math.exp(0.1/math.sqrt(10*r)), -X[1]*a/math.sqrt(r)**3 + 0.001*X[1]*math.exp(0.1/math.sqrt(10*r))]
    return [-X[0]*a/math.sqrt(r)**3 , -X[1]*a/math.sqrt(r)**3 ]
sigma = 30.1
epsilon = 100
# def force(a ,X):
    # return [-4*epsilon*(sigma**12*2*X[0]/(X[0]*X[0] + X[1]*X[1])**7 - sigma**6*2*X[0]/(X[0]*X[0] + X[1]*X[1])**4), -4*epsilon*(sigma**12*2*X[1]/(X[0]*X[0] + X[1]*X[1])**7 - sigma**6*2*X[1]/(X[0]*X[0] + X[1]*X[1])**4)] 

def forces(xys, k):
    sumForce = [0,0]
    for i in range(len(xys)):
        if k != i:
            distVec = [xys[k][0] - xys[i][0], xys[k][1] - xys[i][1]]
            myForce = force(epsilon, distVec)
            sumForce[0] = myForce[0]
            sumForce[1] = myForce[1]
    return sumForce

def nextVel(xys,dt,k):
    itForce = forces(xys,k)
    print(itForce)

    if abs(xys[k][0]) > boxSize:
        xys[k][2] = -xys[k][2]
    if abs(xys[k][1]) > boxSize:
        xys[k][3] = -xys[k][3]

    speed = math.sqrt(xys[k][2]**2 + xys[k][3]**2)
    if speed > 5:
        xys[k][2] /= 1.5
        xys[k][3] /= 1.5
    # elif speed < 0.1:
        # xys[k][2] *= 1.5
        # xys[k][3] *= 1.5
    return [itForce[0]*dt + xys[k][2] , itForce[1]*dt + xys[k][3] ]

def nextPosVel(xys,dt,k):
    itVelocity = nextVel(xyz, dt, k)
    return [itVelocity[0]*dt  + xys[k][0] , itVelocity[1]*dt + xys[k][1], itVelocity[0], itVelocity[1]]


def nextPoses(xys,dt):
    newPoses = []
    for i in range(len(xyz)):
        newPoses.append(nextPosVel(xyz,dt,i))
    return newPoses

if __name__=='__main__':
    spread= 100
    spreadV=  1
    closest = 10
    xyz = [[random.uniform(-spread,spread), random.uniform(-spread,spread), random.uniform(-spreadV, spreadV), random.uniform(-spreadV, spreadV) ]]
    print(xyz)
    atomN =5
    addQ = True
    for k in range(0, atomN):
        a = [random.uniform(-spread,spread), random.uniform(-spread,spread), random.uniform(-spreadV, spreadV), random.uniform(-spreadV, spreadV) ]
        addQ = True
        for X in xyz:
            if (a[0] - X[0])**2 + (a[1] - X[1])**2 < closest*closest:
                addQ = False
        if addQ:
            xyz.append(a)
     

    saveInt = 0
    for t in range(10000000):
        xyz = nextPoses(xyz, 0.0001)
        if t % 1000 == 0:  
            # fig, axs = plt.figure(figsize=(12, 6))
            plt.xlim(-spread, spread)
            plt.ylim(-spread, spread)
            print(len(xyz), '', t/1000, xyz)
            x, y, vx, vy = np.array(xyz).T

            plt.scatter(x,y)
            plt.savefig('Images/test' + "{:03d}".format(saveInt) + '.png')
            im = Image.open('Images/test' + "{:03d}".format(saveInt) + '.png')
            rgb_im = im.convert('RGB')
            rgb_im.save('Images/test' + "{:03d}".format(saveInt) + '.jpg')
            plt.clf()
            saveInt += 1




