import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patch


def add_net(max, min):
    for x in range(min, max):
        plt.gca().add_patch(patch.Rectangle((x, min), 0.0000000001, max, color='#000000', fill=True))
    for y in range(min, max):
        plt.gca().add_patch(patch.Rectangle((min, y), max, 0.0000000001, color='#000000', fill=True))
    pass


def bresenham_line(x0, y0, x1, y1):
    x_points = np.empty(0)
    y_points = np.empty(0)

    steep = abs(x1 - x0) > abs(y1 - y0)
    if steep:
        y0, x0 = x0, y0
        y1, x1 = x1, y1

    if y0 > y1:
        y0, y1 = y1, y0
        x0, x1 = x1, x0

    if x0 < x1:
        ystep = 1
    else:
        ystep = -1

    deltax = y1 - y0
    deltay = abs(x1 - x0)
    error = -deltax / 2
    y = x0

    for x in range(y0, y1 + 1):
        if steep:
            x_points = np.append(x_points, x)
            y_points = np.append(y_points, y)
        else:
            x_points = np.append(x_points, y)
            y_points = np.append(y_points, x)

        error = error + deltay
        if error > 0:
            y = y + ystep
            error = error - deltax
    return x_points, y_points


if __name__ == '__main__':

    # x0,y0,x1,y1
    coord = np.array([6, 19, 12, 16])

    if coord.size != 4:
        raise Exception("Illegal size of input data")
    if coord.min() == coord.max():
        raise Exception("You can do it yourself (c) Brezenhem")

    (x_pts, y_pts) = bresenham_line(x0=coord[0], y0=coord[1], x1=coord[2], y1=coord[3])

    add_net(min=coord.min()-1, max=coord.max()+1)

    for x, y in zip(x_pts, y_pts):
        plt.gca().add_patch(patch.Rectangle((x, y), 1.0, 1.0, color='#000000', fill=True))

    plt.xlim(coord.min()-1, coord.max()+1)
    plt.ylim(coord.min()-1, coord.max()+1)
    plt.title("(x0,y0)=(%.1f,%.1f)\n(x1,y1)=(%.1f,%.1f) " % (coord[0], coord[1], coord[2], coord[3]))

    # name = "(%.1f,%.1f)_(%.1f,%.1f) " % (coord[0], coord[1], coord[2], coord[3]) + ".jpg"
    # plt.savefig(name, dpi=200)
    plt.show()