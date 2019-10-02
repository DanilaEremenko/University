import numpy as np


def simplex_method(arr, mli, mci):
    res = arr
    for cli in range(0, arr.shape[0]):
        for cci in range(0, arr.shape[1]):
            if cli != mli and cci != mci:
                res[cli][cci] = arr[cli][cci] * arr[mli][mci] - arr[mli][cci] * arr[cli][mci]
    old_op = arr[mli][mci]
    res[mli:mli + 1] = arr[mli:mli + 1] * (-1)
    arr[mli][mci] = 1
    res /= old_op
    return res
