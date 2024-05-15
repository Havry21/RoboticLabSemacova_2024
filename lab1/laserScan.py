import math
import numpy as np
import matplotlib.pyplot as plt

def calculateTransformationMatrix(angle, position_vector):
    # матрица поворота
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle), 0],
                                [np.sin(angle), np.cos(angle), 0],
                                [0, 0, 1]])
        
    # матрица перемещения
    translation_matrix = np.array([[1, 0, position_vector[0]],
                                   [0, 1, position_vector[1]],
                                   [0, 0, 1]])
    return np.dot(translation_matrix, rotation_matrix)

scan = np.loadtxt('laserscan.dat')
angle = np.linspace(-math.pi/2, math.pi/2, np.shape(scan)[0], endpoint='true')
pi = math.pi

x = []
y = []


for s, a in zip(scan, angle):
    x.append(s * math.cos(a))
    y.append(s * math.sin(a)) 
    

fig, (pl1,pl2) = plt.subplots(1,2)
pl1.scatter(x,y)
pl1.set_title("Local")
pl1.set_aspect('equal')
#plt.show()

globalRobotCoord = np.array([1, 0.5, pi/2])
localLaserCoord = np.array([0.2, 0, pi])


TglobaltoRobot = calculateTransformationMatrix(globalRobotCoord[2], globalRobotCoord[:2])
TrobotToLaser = calculateTransformationMatrix(localLaserCoord[2], localLaserCoord[:2])
T = np.matmul(TglobaltoRobot, TrobotToLaser)

w = np.ones(len(x))
localScanLaser = np.array([x,y,w])
globalScanLaser = np.matmul(T,localScanLaser)

pl2.scatter(globalScanLaser[0,:],globalScanLaser[1,:])
pl2.plot(globalRobotCoord[0],globalRobotCoord[1], 'or')
pl2.plot(T[0,2],T[1,2],'+r')
pl2.set_title("Global")
pl2.set_aspect('equal')

plt.show()


