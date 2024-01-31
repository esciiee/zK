import numpy as np
from scipy.interpolate import lagrange
from random import randint

# hadamard product of two vectors is homomorphic to polynomial multiplication

# the product polynomials of two vectors will still interpolate the polynomial multiplication for x = 1 to n
# we care about x = 1, 2, 3

a, b, c, d, e, f = [randint(-1000, 1000) for _ in range(6)]

x = np.array([1, 2, 3])
y1 = np.array([a, b, c])
y2 = np.array([d, e, f])

poly1 = lagrange(x, y1)
poly2 = lagrange(x, y2)

polyx = lagrange(x, y1 * y2)

poly3 = poly1 * poly2

assert poly3(1) == y1[0] * y2[0]
assert poly3(2) == y1[1] * y2[1]
assert poly3(3) == y1[2] * y2[2]