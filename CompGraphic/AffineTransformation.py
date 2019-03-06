import numpy as np
from math import sin, cos, pi

C_ARR = np.array([True, False, False])

# 1 Example
# Swap to 90
if C_ARR[0]:
    print('\n--------------Example1-------------\n')
    A_p = np.matrix([5, 8, 1]).T
    B_p = np.matrix([5, 5, 1]).T
    C_p = np.matrix([10, 5, 1]).T
    angle = pi / 2

    A = np.matrix([[1, 0, -int(A_p[0])],
                   [0, 1, -int(A_p[1])],
                   [0, 0, 1]])
    B = np.matrix([[int(cos(angle)), int(sin(angle)), 0],
                   [int(-sin(angle)), int(-cos(angle)), 0],
                   [0, 0, 1]])  # cos,sin,-sin,-cos
    C = np.matrix([[1, 0, int(A_p[0])],
                   [0, 1, int(A_p[1])],
                   [0, 0, 1]])  # ~A

    D = C * B * A

    print("D = \n", D)

    A_r = D * A_p
    B_r = D * B_p
    C_r = D * C_p

if C_ARR[1]:
    # 2 Example
    print('\n--------------Example2-------------\n')
    # Defult matrix
    C = np.matrix([[2, 5, 1], [5, 5, 1], [5, 10, 1]])
    # TargetMatrix
    TM = np.matrix([[5, 8, 1], [5, 5, 1], [10, 5, 1]])

    f = 1.0 / np.linalg.det(C) * TM
    print("f = \n", f)

if C_ARR[2]:
    # 3 Example
    print('\n--------------Example3-------------\n')
    # Default Points
    A_p1 = np.matrix([0, 2, 1])
    B_p1 = np.matrix([0, 6, 1])
    C_p1 = np.matrix([6, 6, 1])
    D_p1 = np.matrix([6, 2, 1])

    P_matrix1 = np.matrix([[0, 6, 1], [6, 6, 1], [6, 2, 1]])

    # Target Points
    B_p2 = np.matrix([0, -5, 1])
    C_p2 = np.matrix([3, -5, 1])
    D_p2 = np.matrix([3, 0, 1])

    P_matrix2 = np.matrix([[0, -5, 1], [3, -5, 1], [3, 0, 1]])

    # Changing Function
    f = P_matrix1.I * P_matrix2
    print('P1(-1) = \n', P_matrix1.I, '\n')

    print('f = \n', f)
