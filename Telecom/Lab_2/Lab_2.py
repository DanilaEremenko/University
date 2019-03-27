from __future__ import print_function
from timeit import default_timer as timer
from Telecom.my_telecom import *

if __name__ == '__main__':
    show = True
    sig = np.array([0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0])
    mess = np.array([1, 0, 1])
    p_size = 8

    plot_graphic(x=np.arange(0, sig.__len__(), 1), y=sig,
                 title='signal', show=True)

    # sig_noise = sig + np.random.randn(len(sig))

    for method in ['fft', 'direct', 'auto']:
        t = timer()
        corr = signal.correlate(sig, mess, mode='full', method=method)
        elapsed = timer() - t
        plot_graphic(x=np.arange(0, corr.__len__(), 1), y=corr,
                     title='correlation %s\ntime = %.5f' % (method, elapsed),
                     show=True)

    sy_mess_i = 0
    max = 0
    i = 0
    for n in corr:
        if n > max:
            max = n
            sy_mess_i = i
        i += 1

    p_start = sy_mess_i + mess.__len__()
    p_end = p_start + p_size
    p = sig[p_start:p_end]

    print("sync mess start= ", sy_mess_i)
    print("package = ", p)

    plot_graphic(x=np.arange(0, sig.__len__(), 1), y=sig)
    plot_graphic(x=np.arange(sy_mess_i, sy_mess_i + 3, 1), y=mess)
    plot_graphic(x=np.arange(p_start, p_end, 1), y=p,
                 title='package')
    plt.legend(('signal', 'sync mess','package'), loc='upper right', shadow=True)

    plt.show()
