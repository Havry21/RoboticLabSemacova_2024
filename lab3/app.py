import math
import numpy as np
import matplotlib.pyplot as plt


def diffdrive(x, y, theta, v_l, v_r, t, l):
    if v_r == v_l:
        theta_n = theta
        x_n = x + v_l * t * np.cos(theta)
        y_n = y + v_l * t * np.sin(theta)
    else:
        R = l / 2 * ((v_r + v_l) / (v_r - v_l))
        ICC = np.array([x - R * math.sin(theta), y + R * math.cos(theta)])
        w = (v_r - v_l) / l
        angle = w * t
        rotation_matrix = np.array([[np.cos(angle), -np.sin(angle), 0],
                                    [np.sin(angle), np.cos(angle), 0],
                                    [0, 0, 1]])

        t = np.array([[x - ICC[0]], [y - ICC[1]], [theta]])
        t1 = np.array([[ICC[0]], [ICC[1]], [angle]])

        result = np.dot(rotation_matrix, t) + t1
        x_n = result[0, 0]
        y_n = result[1, 0]
        theta_n = result[2, 0]
    return x_n, y_n, theta_n


def main():
    plt.gca().set_aspect("equal")
    pi = math.pi
    t = 0.5
    pos = [[1.5, 2.0, pi / 2]]
    c = [[0.3, 0.3, 3], [0.1, -0.1, 1], [0.2, 0, 2]]
    for i in c:
        plt.quiver(pos[-1][0], pos[-1][1], np.cos(pos[-1][2]), np.sin(pos[-1][2]))
        newPose = diffdrive(pos[-1][0], pos[-1][1], pos[-1][2], i[0], i[1], i[2], 0.5)
        print(newPose)
        pos.append(newPose)

    plt.quiver(pos[-1][0], pos[-1][1], np.cos(pos[-1][2]), np.sin(pos[-1][2]))

    plt.xlim([1, 2])
    plt.ylim([1.5, 3.5])
    plt.show()


if __name__ == '__main__':
    main()
