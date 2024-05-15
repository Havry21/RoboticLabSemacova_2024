import math
import numpy
import matplotlib.pyplot as plt


def discrete_bayes_filter(bel, d):
    n = 0

    new_bel = bel

    if d == 1:
        for x in range(len(bel)):
            new_bel[x] = bel[x] * 0.25
            if x == len(bel):
                new_bel[x] += bel[x - 1] * 0.75
            else:
                if x > 0: new_bel[x] += bel[x - 1] * 0.5
                else: new_bel[x] = 0

                if x > 1: new_bel[x] += bel[x - 2] * 0.5
                else: new_bel[x] = 0

            n += new_bel[x]

    else:
        for x in range(len(bel)):
            new_bel[x] = bel[x] * 0.25
            if x == 0:
                new_bel[x] += bel[x + 1] * 0.75
            else:
                if x < len(bel)-1:
                    new_bel[x] += bel[x + 1] * 0.5
                else:
                    new_bel[x] = 0

                if x < len(bel)-2:
                    new_bel[x] += bel[x + 2] * 0.25
                else:
                    new_bel[x] = 0

            n += new_bel[x]

    for x in range(len(bel)):
        new_bel[x] = bel[x] / n

    return new_bel


def drawPlot(bel):
    plt.cla()
    plt.bar(range(len(bel)), bel, width=1.0)
    plt.axis([0, len(bel), 0, 0.5])
    plt.draw()
    plt.pause(0.1)


def main():
    plt.figure()
    plt.ion()
    plt.show()

    bel = numpy.hstack((numpy.zeros(9), 1, numpy.zeros(10)))
    while True:
        for i in range(0, 9):
            discrete_bayes_filter(bel, 1)
            drawPlot(bel)
            print(f"summ - {numpy.sum(bel)}")

        for i in range(0, 9):
            discrete_bayes_filter(bel, 0)
            drawPlot(bel)
            print(f"summ - {numpy.sum(bel)}")


if __name__ == '__main__':
    main()
