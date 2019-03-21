from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    signal = np.array([0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0])
    mess = np.array([1, 0, 1])
    pack_len = 8

    plt.plot(signal)
    plt.title("signal")
    plt.show()

    for mode in ['same', 'full', 'valid']:
        pack_cor = np.correlate(signal, mess, mode=mode)
        plt.plot(pack_cor)
        plt.title(mode)
        plt.show()

    print("first pack   = \n", signal[0:pack_len])
    print("second pac   = \n", signal[pack_len:signal.__len__()])
