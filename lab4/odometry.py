import math
import numpy as np
from scipy. stats import norm
import timeit
import matplotlib.pyplot as plt

def sample_normal_distribution(b):
    return np.random.normal(0,b)
    return 0.5 * np.sum(np.random.uniform(-b,b, 12)) 

def sample_Odometry_Motion_Model(x,u,a):
    new_u = u
    new_u[0] += sample_normal_distribution(a[0] * abs(u[0])+ a[1] * u[2])
    new_u[1] += sample_normal_distribution(a[0] * abs(u[1])+ a[1] * u[2])
    new_u[2] += sample_normal_distribution(a[2] * u[2]+ a[3] * (abs(u[0]) + abs(u[1])))
    new_x = x
    new_x[0] += new_u[2]*math.cos(x[2] + new_u[0])
    new_x[1] += new_u[2]*math.sin(x[2] + new_u[0])
    new_x[2] += new_u[0] + new_u[1]
    return new_x

def main():
    plt.figure()
    x = [2, 4, 0]
    u = [np.pi/2, 0, 1]
    a = [0.05, 0.05, 0.01, 0.01]
    for i in range(500):
        new_x = sample_Odometry_Motion_Model(x,u,a)
        print(f"{new_x}")
        plt.plot(new_x[0], new_x[1],color='r', marker='.')
        
    plt.plot(x[0], x[1], color=(0., 0, 0), marker='x')
    plt.show()
    
if __name__ == '__main__':
    main()
