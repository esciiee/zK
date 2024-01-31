import numpy as np
from scipy.interpolate import lagrange

# polynomial : polynomial with positive degree and real coefficients whose y values  interpolate
# the vector at x = 1 to n  where n is the dimension/lenght of the vector

# vector: a vector can also be conceptualized as each entry containing a pair of values (x, y) 
# whose x value is the dimension and y value is the vector at that dimension

# adding two vector is homomorphic to adding two polynomials

x = np.array([1, 2, 3])
y1 = np.array([1,0, 1])
y2 = np.array([-1, 5, 3])

poly1 = lagrange(x, y1)
poly2 = lagrange(x, y2)

poly3 = poly1 + poly2

assert all(poly3(x) == y1[i] + y2[i] for i, x in enumerate(range(1, 4)))