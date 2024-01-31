import numpy as np
from scipy.interpolate import lagrange

# mutiplying a vector by a scalar is homomorphic to multiplying a polynomial by a scalar

x = np.array([1, 2, 3])
y = np.array([4, 12, 6])
y1 = np.array([4, 12, 6]) * 2

poly1 = lagrange(x, y)
poly2 = lagrange(x, y1)

assert all(poly1(x) * 2 == poly2(x) for x in range(1, 4))