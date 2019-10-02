import numpy as np
import sapr_functions as sf

# --------------------------------------------
arr = np.array([[-1, -0.5, 0, 10.1],
                [-1, 0.5, 1, 5.3],
                [1, -0.5, -1, -5.3]
                ])

res_aw = np.array([[1, -1, -1, 4.8],
                   [-1, 0.5, 1, 5.3],
                   [-1, 0, 0, 0]])

res = sf.simplex_method(arr=arr, mli=1, mci=0)

assert res.__eq__(res_aw).all()

# --------------------------------------------
arr = np.array([[-1, -1, 4.8],
                [0.5, 1, 5.3],
                [2, 1, 5.3]
                ])

res_aw = np.array([[-1, -1, 4.8],
                   [-0.5, 0.5, 7.699999999999999],
                   [-2, -1, 14.899999999999999]])

res = sf.simplex_method(arr=arr, mli=0, mci=0)

assert res.__eq__(res_aw).all()

# ------------------------------------------
arr = np.array([[-1, -2, 0, 5.3],
                [-1, 2, 1, 2.8],
                [1, -2, -1, -2.8]
                ])

res = sf.simplex_method(arr=arr, mli=1, mci=0)

print(res)

arr = np.array([[-4, -1, 2.5],
                [2, 1, 2.8],
                [3, 1, 2.8]])

res = sf.simplex_method(arr=arr, mli=0, mci=0)

print(res)
