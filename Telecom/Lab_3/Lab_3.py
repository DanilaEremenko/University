from __future__ import print_function
from Telecom.my_telecom import *
from scipy import signal

if __name__ == '__main__':
    # Parameters of signals
    sig_freq = 20  # frequency of original signal
    T = 1.0 / sig_freq
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
        xlim=[0, 1], ylim=[-4, 3],
        show=True)

    # noise signal-----------------------------------------------------------------------
    sig_noise = sig + np.random.randn(len(sig))

    plot_graphic(
        x=t[:int((n - 1) / 2)], y=sig_noise[:int((n - 1) / 2)],
        title='noise signal ',
        x_label='time(S)', y_label='amplitude (V)',
        xlim=[0, 1], ylim=[-4, 3],
        show=True
    )

    # noise signal spectrum--------------------------------------------------------------
    fft_freq = np.fft.fftfreq(n, ts)  # discrete Fourier Transform frequencies
    sig_fft = np.fft.fft(sig_noise) / n * 2  # discrete Fourier Transform ( / n * 2 - normalization)

    plot_graphic(
        x=fft_freq[:int((n - 1) / 2)], y=abs(sig_fft)[:int((n - 1) / 2)],
        title='spectrum of noise signal',
        x_label='frequency (Hz)', y_label='amplitude (V)',
        xlim=[0, 150],
        show=True
    )

    # Nyquist freequency
    nyq = 0.5 * fs
    Wn = 2 * 2 * sig_freq / nyq
    N = 4

    for btype in ['lowpass', 'highpass']:
        # create filter
        fnum, fdenom = signal.butter(N=N, Wn=Wn, btype=btype)

        # filter signal
        filtered = signal.filtfilt(fnum, fdenom, sig_noise)

        plot_graphic(
            x=t[:int((n - 1) / 2)], y=filtered[:int((n - 1) / 2)],
            title='filtered signal\nbtype = %s, N = %d' % (btype, N),
            x_label='time(S)', y_label='signal',
            xlim=[0, 1], ylim=[-4, 3],
            show=True)

        # calculate spectrum
        fft_freq = np.fft.fftfreq(n, ts)  # discrete Fourier Transform frequencies
        sig_fft = np.fft.fft(filtered) / n * 2  # discrete Fourier Transform ( / n * 2 - normalization)

        plot_graphic(
            x=fft_freq[:int((n - 1) / 2)], y=abs(sig_fft)[:int((n - 1) / 2)],
            title='spectrum of filtered signal\nbtype = %s, N = %d' % (btype, N),
            x_label='frequency (Hz)', y_label='amplitude (V)',
            xlim=[0, 150],
            show=True
        )
