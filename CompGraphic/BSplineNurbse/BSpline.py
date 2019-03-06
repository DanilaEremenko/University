import matplotlib.pyplot as plt
from math import pow
import numpy as np


def geta(t, a=0):
    return 1.0 / 2.0 * pow(t - a, 2)


def getb(t, b=0):
    return 3.0 / 4.0 - pow(t - b - 1.5, 2)


def getc(t, c=0):
    return 1.0 / 2.0 * pow(t - c - 3, 2)


def getPt(p0, p1, p2, a, b, c):
    return c * p0 + b * p1 + a * p2


if __name__ == '__main__':
    # labels on graphic
    X_SHIFT = 0.9
    Y_SHIFT = 1.1
    F_SIZE = 12

    # Input data
    px = np.array([0, 5, 5, 9])
    py = np.array([4, 8, -2, 2])
    h = 0.5

    # Incorrect input data checking
    if px.__len__() != py.__len__():
        print("ERROR\nUnequal size of input arrays")
        exit(0)

    print("Default poligon\nx\ty")
    for x, y in zip(px, py):
        print(x, '\t', y)

    for i in range(0, px.__len__()):
        plt.text(px[i] * X_SHIFT, py[i] * Y_SHIFT, "p" + str(i), fontsize=F_SIZE)
    plt.plot(px, py, '--o')

    ptx = []
    pty = []

    print("\n[2 , 3]-------------------------------------------")
    for t in np.arange(2, 3.01, h, dtype=float):
        ptx.append(getPt(px[0], px[1], px[2], geta(t, a=2), getb(t, b=1), getc(t, c=0)))
        pty.append(getPt(py[0], py[1], py[2], geta(t, a=2), getb(t, b=1), getc(t, c=0)))
        plt.text(ptx[ptx.__len__() - 1] * X_SHIFT, pty[pty.__len__() - 1] * Y_SHIFT, "pt1_%.3f" % t, fontsize=F_SIZE)
        print("Px(%.3f) = %f" % (t, ptx[ptx.__len__() - 1]))
        print("Py(%.3f) = %f\n" % (t, pty[pty.__len__() - 1]))

    print("[3 , 4]-------------------------------------------")
    for t in np.arange(3.0, 4.01, h, dtype=float):
        ptx.append(getPt(px[1], px[2], px[3], geta(t, a=3), getb(t, b=2), getc(t, c=1)))
        pty.append(getPt(py[1], py[2], py[3], geta(t, a=3), getb(t, b=2), getc(t, c=1)))
        plt.text(ptx[ptx.__len__() - 1] * X_SHIFT, pty[pty.__len__() - 1] * Y_SHIFT, "pt1_%.3f" % t, fontsize=F_SIZE)
        print("Px(%.3f) = %.3f" % (t, ptx[ptx.__len__() - 1]))
        print("Py(%.3f) = %.3f\n" % (t, pty[pty.__len__() - 1]))

    # plot-----------------------------------------------------------------------
    plt.plot(ptx, pty, '--o')

    if (input("SAVE[Y/n]") == "Y"):
        name = input("Name = ")
        plt.savefig("BSplineNurbse/Pictures/" + name, dpi=200)
    if (input("SHOW[Y/n]") == "Y"):
        plt.show()
