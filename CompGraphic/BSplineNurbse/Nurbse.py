import matplotlib.pyplot as plt
import numpy as np


def getN(t, k, T, q):
    if q == 1:
        return 1 if T[k] <= t and t < T[k + 1] else 0
    else:
        sum = 0
        recurs1 = getN(t=t, T=T, k=k, q=q - 1)
        recurs2 = getN(t=t, T=T, k=k + 1, q=q - 1)
        if T[k + q - 1] - T[k] != 0:
            sum += ((t - T[k]) / (T[k + q - 1] - T[k])) * recurs1
        if T[k + q] - T[k + 1] != 0:
            sum += ((T[k + q] - t) / (T[k + q] - T[k + 1])) * recurs2
        return sum


def getPtWithoutN(w0, w1, w2, p0, p1, p2):
    return (w0 * p0 + w1 * p1 + w2 * p2) / (w0 + w1 + w2)


def getPt(t, p0, p1, p2, p3, w0, w1, w2, w3, T, pNumber):
    return (w0 * p0 * getN(t=t, k=0, T=T, q=pNumber - 1) +
            w1 * p1 * getN(t=t, k=1, T=T, q=pNumber - 1) +
            w2 * p2 * getN(t=t, k=2, T=T, q=pNumber - 1) +
            w3 * p3 * getN(t=t, k=3, T=T, q=pNumber - 1)
            ) / \
           (w0 * getN(t=t, k=0, T=T, q=pNumber - 1) +
            w1 * getN(t=t, k=1, T=T, q=pNumber - 1) +
            w2 * getN(t=t, k=2, T=T, q=pNumber - 1) +
            w3 * getN(t=t, k=3, T=T, q=pNumber - 1))


if __name__ == '__main__':
    # labels on graphic
    X_SHIFT = 0.9
    Y_SHIFT = 1.1
    F_SIZE = 12

    # Input data
    tBottom = 2
    tTop = 4
    px = np.array([0, 5, 5, 9])
    py = np.array([4, 8, -2, 2])
    h = 0.25
    w = np.array([1.25, 1.5, 1.75, 2.5])

    # Incorrect input data checking
    if px.__len__() != py.__len__() or px.__len__() != w.__len__():
        print("ERROR\nUnequal size of input arrays")
        exit(0)

    POINTS_NUMBER = px.__len__()

    print("Default poligon\nx\ty")
    for x, y in zip(px, py):
        print(x, '\t', y)

    for cycleNum in range(0, px.__len__()):
        plt.text(px[cycleNum] * X_SHIFT, py[cycleNum] * Y_SHIFT, "p" + str(cycleNum), fontsize=F_SIZE)
    plt.plot(px, py, '--o')

    ptx = []
    pty = []
    print("\np(t) calculating-------------------------------------------\n")

    # TODO README
    # IF h<=0.25 -> MODE = N
    # IF h>0.25 - > MODE = WN
    mode = 'N'
    if mode == 'N':
        T = np.arange(tBottom, tTop + 0.01, 0.25, dtype=float)
        for t in np.arange(tBottom, tTop + 0.01, h, dtype=float):
            xPt = getPt(t, px[0], px[1], px[2], px[3], w[0], w[1], w[2], w[3], T, POINTS_NUMBER)
            yPt = getPt(t, py[0], py[1], py[2], py[3], w[0], w[1], w[2], w[3], T, POINTS_NUMBER)
            if (not np.isnan(xPt) and not np.isnan(yPt)):
                ptx.append(xPt)
                pty.append(yPt)
                plt.text(ptx[ptx.__len__() - 1] * X_SHIFT, pty[pty.__len__() - 1] * Y_SHIFT, "pt(%.3f)" % t,
                         fontsize=F_SIZE)
                print("Px(%.3f) = %.3f" % (t, ptx[ptx.__len__() - 1]))
                print("Py(%.3f) = %.3f\n" % (t, pty[pty.__len__() - 1]))
    elif mode == 'WN':
        cycleNum = POINTS_NUMBER - 2
        i = 0
        while cycleNum > 0:
            ptx.append(
                getPtWithoutN(w0=w[i], w1=w[i + 1], w2=w[i + 2], p0=px[i], p1=px[i + 1], p2=px[i + 2]))
            pty.append(
                getPtWithoutN(w0=w[i], w1=w[i + 1], w2=w[i + 2], p0=py[i], p1=py[i + 1], p2=py[i + 2]))
            plt.text(ptx[ptx.__len__() - 1] * X_SHIFT, pty[pty.__len__() - 1] * Y_SHIFT, "pt_%.d" % i, fontsize=F_SIZE)
            print("Px%.d = %.3f\n" % (i, ptx[ptx.__len__() - 1]))
            print("Py%.d = %.3f\n" % (i, pty[pty.__len__() - 1]))
            cycleNum -= 1
            i += 1

    # plot-----------------------------------------------------------------------
    plt.plot(ptx, pty, '--o')

    if (input("SAVE[Y/n]") == "Y"):
        name = input("Name = ")
        plt.savefig("Pictures/" + name, dpi=200)
    if (input("SHOW[Y/n]") == "Y"):
        plt.show()
