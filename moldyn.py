import numpy as np
import math


def force(a ,X):
    return [-X[0]*a/math.sqrt(X[0]*X[0] + X[1]*X[1])**3, -X[1]*a/math.sqrt(X[0]*X[0] + X[1]*X[1])**3]

def forces(xys, k):
    sumForce = [0,0]
    for i in range(len(xys)):
        if k != i:
            distVec = (xys[k][0] - xys[i][0], xys[k][1] - xys[i][1])
            myForce = force(0.1, distVec)
            sumForce[0] = myForce[0]
            sumForce[1] = myForce[1]
    return sumForce

def nextPos(xys,dt,k):
    itForce = forces(xys,k)
    return [itForce[0]*dt*dt + xys[k][0] , itForce[1]*dt*dt + xys[k][1] ]


def nextPoses(xys,dt):
    newPoses = []
    for i in range(len(xyz)):
        newPoses.append(nextPos(xyz,dt,i))
    return newPoses

if __name__=='__main__':
    xyz = [[0,0], [1,1], [1,0]]
    for t in range(1000000):
        xyz = nextPoses(xyz, 0.0001)
        if t % 100 == 0:  
            print(xyz)




