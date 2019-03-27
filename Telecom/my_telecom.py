# Package containing common part and useful functions for labs

import matplotlib.pyplot as plt
from scipy import signal
import numpy as np


def get_sin_sig(t, freq, ampl):
    """
    :return: ampl * sin(freeq * t) + ampl * sin(2 * freeq * t)
    """
    return ampl * np.sin(2 * np.pi * freq * t) + ampl * np.cos(2 * 2 * np.pi * freq * t)


def get_rect_sig(t, freq, ampl):
    """
    :return: ampl * signal.square(2 * np.pi * freq * t)
    """
    return ampl * signal.square(2 * np.pi * freq * t)


def get_triang_sig(t, freq, ampl):
    """
    :return: ampl * signal.sawtooth(2 * np.pi * freq * t)
    """
    return ampl * signal.sawtooth(2 * np.pi * freq * t)


def plot_graphic(x, y, title=None, x_label="x", y_label="y", gr_form='-', xlim=None, ylim=None, show=False, save=False):
    """
    just my function for comfortable plotting
    """
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    if title != None:
        plt.title(title)

    plt.plot(x, y, gr_form)

    if xlim != None:
        plt.xlim(xlim[0], xlim[1])
    if ylim != None:
        plt.ylim(ylim[0], ylim[1])

    if show:
        plt.show()
    if save:
        plt.savefig(title + '.png')
        plt.close()
