import math
import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


def likelihood(x, y):
    x0 = np.array([12, 4])
    x1 = np.array([5, 7])
    d0 = 3.9
    d1 = 4.5
    q0 = 1
    q1 = 1.5
    P = []

    for i in range(x.size):
        xy = [x[i], y[i]]
        pdf_0 = scipy.stats.norm.pdf(d0, math.sqrt(np.sum(np.square(xy - x0))), math.sqrt(q0))
        pdf_1 = scipy.stats.norm.pdf(d1, math.sqrt(np.sum(np.square(xy - x1))), math.sqrt(q1))
        P.append(pdf_0 * pdf_1)

    return P


def main():
    m_0 = np.array([10, 8])
    m_1 = np.array([6, 3])
    x_0 = np.array([12, 4])
    x_1 = np.array([5, 7])

    x = np.arange(2.5, 13.0, 0.5)
    y = np.arange(2.5, 13.0, 0.5)

    X, Y = np.meshgrid(x, y)
    Z = np.array(likelihood(X.flatten(), Y.flatten())).reshape(X.shape)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, alpha=0.5)

    ax.scatter(m_0[0], m_0[1], 0, c='g', marker='o', s=100)
    ax.scatter(m_1[0], m_1[1], 0, c='r', marker='o', s=100)
    ax.scatter(x_0[0], x_0[1], 0, c='g', marker='^', s=100)
    ax.scatter(x_1[0], x_1[1], 0, c='r', marker='^', s=100)
    plt.show()


if __name__ == '__main__':
    main()
