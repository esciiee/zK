from scipy.interpolate import lagrange
import numpy as np

# say for n = 3 and x = [1, 2, 3] and we are encoding for the vector v = [4, 12, 6]

# task : interpolate the polynomial for (1, 4), (2, 12), (3, 6) and verify against the values of v for x = 1, 2, 3

x = np.array([1, 2, 3])
y = np.array([4, 12, 6])

poly = lagrange(x, y)

# print(poly)

assert poly(1) == 4
assert poly(2) == 12
assert poly(3) == 6

x = np.array([1,2,3])
y = np.array([4,5,6])

polyc = lagrange(x, y)
print(polyc)