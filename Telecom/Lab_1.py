from __future__ import print_function
import matplotlib.pyplot as plt
import numpy as np


def get_sin_sig(t, freeq, ampl):
    return ampl * np.cos(2 * np.pi * freeq * t) + ampl * np.cos(2 * 2 * np.pi * freeq * t)


def get_rect_sig(t, freeq, ampl):
    return ampl * np.sign(get_sin_sig(t, freeq, ampl))


def plot_graphic(x, y, title, x_label="x", y_label="y", show=False, save=False):
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.plot(x, y)
    if show:
        plt.show()
    if save:
        plt.savefig(title + '.png')
        plt.close()


if __name__ == '__main__':

    freeq = 20
    ampl = 2
    fs = 1000  # sampling rate
    ts = 1.0 / fs  # sampling interval
    n = 1 << 13  # number of fft points, pick power of 2
    t = np.arange(0, n * ts, ts)  # time vector
    pts_num = 100
    signals = [get_sin_sig(t, freeq, ampl), get_rect_sig(t, freeq, ampl)]
    functions = ['sinus_', 'rectangle_']
    show = True
    save = not show

    for sig, title in zip(signals, functions):
        sig_fft = np.fft.fft(sig) / n * 2  # discrete Fourier Transform
        fft_freq = np.fft.fftfreq(n, ts)  # discrete Fourier Transform frequencies

        plot_graphic(x=t[:fs], y=sig[:fs], title=title + 'signal', x_label='time(S)',
                     y_label='signal',
                     show=show, save=save)
        plot_graphic(x=fft_freq[:fs], y=abs(sig_fft)[:fs], title=title + 'spectrum', x_label='frequency (Hz)',
                     y_label='amplitude (V)',
                     show=show, save=save)
