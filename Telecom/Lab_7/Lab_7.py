import sys

sys.path.append("addition")

import numpy as np
from BinarySymmetricChannel import BSC
from GaloisField import GaloisField
from GaloisField import GF2
from LinearBlockCode import LinearBlockCode
from CyclicCode import CyclicCode
from BCHCode import BCHCode
from numpy import poly1d


# -------------------------- hamming ------------------------------------------
def hamming(m):
    b0 = parity(m, [0, 2, 3])
    b1 = parity(m, [0, 1, 3])
    b2 = parity(m, [0, 1, 2])

    return [b0, b1, m[3], b2, m[2], m[1], m[0]]


def parity(s, indexes):
    return int(s[indexes[0]]) ^ int(s[indexes[1]]) ^ int(s[indexes[2]])


def syndrome(num, indexes):
    return int(num[indexes[0]]) ^ int(num[indexes[1]]) ^ int(num[indexes[2]] ^ int(num[indexes[3]]))


def full_syndrome(m):
    s0 = syndrome(m, [0, 2, 4, 6])
    s1 = syndrome(m, [1, 2, 5, 6])
    s2 = syndrome(m, [3, 4, 5, 6])
    return np.array([s2, s1, s0])


def coomon_fix(m, syndrome):
    mistake = syndrome[0] * 4 + syndrome[1] * 2 + syndrome[2] - 1
    if mistake == 0:
        return m
    result = m
    result[mistake] = 0 if result[mistake] == 1 else 1
    return result


# -------------------------- hamming matrix ------------------------------------------
ib = np.matrix([[1, 0, 0, 0, 1, 1, 0],
                [0, 1, 0, 0, 1, 0, 1],
                [0, 0, 1, 0, 0, 1, 1],
                [0, 0, 0, 1, 1, 1, 1]])

ht = np.matrix([[0, 1, 1],
                [1, 0, 1],
                [1, 1, 0],
                [1, 1, 1],
                [0, 0, 1],
                [0, 1, 0],
                [1, 0, 0]]
               )


def normalization(matrix):
    for i in range(matrix.__len__()):
        matrix[i] = matrix[i] % 2
    return matrix


def matrix_fix(m, syndrome):
    mistake = syndrome[0, 0] * 4 + syndrome[0, 1] * 2 + syndrome[0, 2]
    if mistake == 1:
        mistake = 4
    elif mistake == 2:
        mistake = 5
    elif mistake == 3:
        mistake = 0
    elif mistake == 4:
        mistake = 6
    elif mistake == 5:
        mistake = 1
    elif mistake == 6:
        mistake = 2
    elif mistake == 7:
        mistake = 3
    if mistake == 0:
        return m
    result = m
    result[0, mistake] = 0 if result[0, mistake] == 1 else 1
    return result


if __name__ == '__main__':
    # -------------------------- hamming ------------------------------------------
    print("\n-------------- hamming ------------------------\n")
    message = np.array([1, 0, 1, 0])
    hamming = hamming(message)

    print("message: ", message)
    print("hamming code for this message: ", hamming)
    print("syndrome for this code: ", full_syndrome(hamming))
    hamming[4] = 0 if hamming[4] == 1 else 1
    print("make mistake in 5 digit: ", hamming)
    print("syndrome for code with error: ", full_syndrome(hamming))
    print("fix the mistake: ", coomon_fix(hamming, full_syndrome(hamming)))

    # -------------------------- hamming matrix ------------------------------------------
    print("\n\n\n-------------- hamming matrix ------------------------\n")

    g = np.matrix([[0, 1, 0, 1]])

    print("message: ", g)

    hamming = g * ib
    hamming.transpose()
    hamming = normalization(hamming)

    print("hamming code for this message: ", hamming)

    syndrome = hamming * ht
    syndrome.transpose()
    syndrome = normalization(syndrome)

    print("syndrome for this code: ", syndrome)

    hamming[0, 4] = 0 if hamming[0, 4] == 1 else 1
    print("make mistake in 5 digit: ", hamming)

    syndrome = hamming * ht
    syndrome.transpose()
    syndrome = normalization(syndrome)

    print("syndrome for code with error: ", syndrome)
    print("fix the mistake: ", matrix_fix(hamming, syndrome))

    # -------------------------- Cyclic code  ------------------------------------------
    print("\n\n\n--------------- Cyclic code ---------------------\n")
    print("CyclicCode")
    """
    A binary linear cyclic code Ccyc(n, k) has code length n = 7 and generator polynomial
    g(X) = 1 + X2 + X3 + X4.

    (a) Find the code rate, the generator and parity check matrices of the code in systematic form, and its Hamming distance.
    (b) If all the information symbols are ‘1’s, what is the corresponding code vector?
    (c) Find the syndrome corresponding to an error in the first information symbol, and show that the code is capable of correcting this error.
    """
    g = np.array([1, 0, 1, 1, 1])
    cc = CyclicCode(g, 7)
    cc.printInfo()

    p = np.array([1, 0, 1, 0, 0, 1])
    gf = GaloisField(p)
    bch = BCHCode(gf, 2)
    bch.printInfo()
    bch.decode(np.poly([1, 1, 0, 1, 1, 1]))
