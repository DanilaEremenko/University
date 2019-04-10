from __future__ import print_function
from Telecom.my_telecom import *
from scipy import signal

if __name__ == '__main__':
    show = True

    # Parameters of signals
    sig_freq = 20  # frequency of original signal
    ampl = 2  # amplitude of original signal
    fs = 1000  # sampling rate
    ts = 1.0 / fs  # sampling interval
    n = 1 << 13  # number of fft points, pick power of 2

    t = np.arange(0, n * ts, step=ts)  # time vector

    sig = get_sin_sig(t, sig_freq, ampl)

    plot_graphic(
        x=t[:int((n - 1) / 2)], y=sig[:int((n - 1) / 2)],
        title='signal',
        x_label='time(S)', y_label='signal',
        xlim=[0, 1],
        show=True)

    sig_noise = sig + np.random.randn(len(sig))

    plot_graphic(
        x=t[:int((n - 1) / 2)], y=sig_noise[:int((n - 1) / 2)],
        title='noise signal',
        x_label='time(S)', y_label='signal',
        xlim=[0, 1],
        show=True
    )

    for N in [ 4, 5, 6]:
        for btype in ['bandstop']:

            # create filter TODO
            fnum, fdenom = signal.butter(N, Wn=[0.019, 0.021], btype=btype)

            # filter the signal TODO
            filtered = signal.filtfilt(fnum, fdenom, sig_noise)

            plot_graphic(x=t[:int((n - 1) / 2)], y=filtered[:int((n - 1) / 2)], x_label='Time',
                         y_label='Amplitude', title='Filtered signal, N = %.d' % N,
                         show=True)
