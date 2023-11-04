import numpy as np
def vec(arr):
    n=np.prod(arr.shape)
    return arr.reshape(n)