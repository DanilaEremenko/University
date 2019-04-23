from __future__ import print_function
from Telecom.my_telecom import *
import numpy as np
from scipy.signal import butter, filtfilt, hilbert

if __name__ == '__main__':
    # ----------------------------- Parameters of signals ------------------------------
    sig_freq = 10  # frequency of original signal
    T = 1.0 / sig_freq
    ampl = 1  # amplitude of original signal
    fs = 2000  # sampling rate
    ts = 1.0 / fs  # sampling interval
    n = 1 << 13  # number of fft points, pick power of 2

    t = np.arange(0, n * ts, step=ts)  # time vector

    sig = ampl * np.sin(2 * np.pi * sig_freq * t)

    # ----------------------------- Parameters of modulation signals ------------------------------
    carrier_freq = 100
    carrier_amplitude = 1
    carrier = np.sin(2 * np.pi * carrier_freq * t)
    m = ampl / carrier_amplitude
    singleton_modulated = (1 + m * ampl * sig) * carrier_amplitude * carrier
    suppressed_carried_mod = ampl * carrier_amplitude * sig * carrier
    single_sideband_mod = hilbert(sig) * np.cos(2 * np.pi * carrier_freq * t) - hilbert(sig) * carrier

    order = 5
    normal_cutoff = sig_freq / carrier_freq

    fnum, fdenom = butter(order, normal_cutoff)
    singleton_demodulated = filtfilt(fnum, fdenom, abs(singleton_modulated))
    suppressed_carried_demod = suppressed_carried_mod * carrier_amplitude * carrier
    # ----------------------------- Parameters of plotting ------------------------------
    sig_xlim = (0, 0.25)

    # ------------------------- spectrum calculating -----------------------------------------
    fft_freq = np.fft.fftfreq(n, ts)  # python function to get Hz frequency axis

    singleton_modulated_fft = \
        abs(np.fft.fft(singleton_modulated)) / n * 2  # discrete Fourier Transform ( / n * 2 - normalization)
    singleton_demodulated_fft = abs(np.fft.fft(singleton_demodulated)) / n * 2

    suppressed_carried_mod_fft = abs(np.fft.fft(suppressed_carried_mod)) / n * 2
    suppressed_carried_demod_fft = abs(np.fft.fft(suppressed_carried_demod)) / n * 2

    single_sideband_mod_fft = abs(np.fft.fft(single_sideband_mod)) / n * 2

    # ------------------------------------------------------------------------
    plot_graphic(t, singleton_modulated,
                 xlim=sig_xlim,
                 x_label='time (s)', y_label='amplitude (V)', show=False)

    plot_graphic(t, singleton_demodulated,
                 xlim=sig_xlim,
                 x_label='time (s)', y_label='amplitude (V)', show=False)

    plt.legend(("Singleton Modulated sine wave", "Singleton Demodulated sine wave"), loc='upper right')
    plt.show()
    # ------------------------------------------------------------------------
    plot_graphic(fft_freq, singleton_modulated_fft,
                 xlim=[0, 200],
                 x_label='frequency (hz)', y_label='amplitude (V)', show=False)

    plot_graphic(fft_freq, singleton_demodulated_fft,
                 xlim=[0, 200],
                 x_label='frequency (hz)', y_label='amplitude (V)', show=False)

    plt.legend(("Singleton Modulated sine wave", "Singleton Demodulated sine wave"), loc='upper right')
    plt.show()
    # -------------------------- Suppressed carrier fft  ---------------------------------------
    plot_graphic(t, suppressed_carried_mod,
                 xlim=sig_xlim,
                 x_label='time (s)', y_label='amplitude (V)', show=False)

    plot_graphic(t, suppressed_carried_demod,
                 xlim=sig_xlim,
                 x_label='time (s)', y_label='amplitude (V)', show=False)

    plt.legend(("Suppressed carrier Modulated sine wave", "Suppressed carrier Demodulated sine wave"),
               loc='upper right')
    plt.show()

    # ------------------------- Suppressed carrier mod & demod fft--------------------------------------------
    plot_graphic(fft_freq, suppressed_carried_mod_fft,
                 xlim=[0, 200],
                 x_label='frequency (hz)', y_label='amplitude (V)', show=False)

    plot_graphic(fft_freq, suppressed_carried_demod_fft,
                 xlim=[0, 200],
                 x_label='frequency (hz)', y_label='amplitude (V)', show=False)

    plt.legend(("Suppressed carrier Modulated sine wave", "Suppressed carrier Demodulated sine wave"),
               loc='upper right')
    plt.show()

    # ------------------------- Single sideband Modulated --------------------------------------------
    plot_graphic(t, single_sideband_mod,
                 xlim=sig_xlim,
                 x_label='time (s)', y_label='amplitude (V)', show=False)

    plt.legend(("Single sideband Modulated sine wave",), loc='upper right')
    plt.show()

    # ------------------------- Single sideband carrier --------------------------------------------
    plot_graphic(fft_freq, single_sideband_mod_fft,
                 xlim=[0, 150],
                 title='Single sideband carrier Modulated sine wave',
                 x_label='frequency (hz)', y_label='amplitude (V)', show=False)

    plt.legend(("Single sideband carrier Modulated sine wave",),loc = 'upper right')
    plt.show()
