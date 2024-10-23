import numpy as np
from tp2 import NDArray

a = NDArray(np.arange(6).reshape(2, 3) + 11)
b = a[1:, 1:]
print("b = a[1:, 1:] =", b)
print("b.base\n", b.base)
print("b.indexed\n", b.indexed)