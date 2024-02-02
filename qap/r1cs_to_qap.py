import numpy as np
import galois
from functools import reduce

# --------------------------- QAP Example --------------------------- #

# eqn : out = x^4 -5*y**2*x**2

# input : x, y
# output : out

# auxillary : v1 = x**2, v2 = v1*v1, v3 = -5y*y

# w = [1, out , x, y, v1, v2, v3]
prime = 79
GF = galois.GF(prime)
def matrix_modulo(matrix):
    """Converts negative values in the matrix to positive values modulo field size."""
    return (matrix % GF.order + GF.order) % GF.order

def interpolate_column(col):
    xs = GF(np.array([1,2,3,4]))
    return galois.lagrange_poly(xs, col)

def handle_coefficient(coefficients):
    if len(coefficients) == 1:
        return np.array([0, 0, 0, 0])
    return coefficients

def inner_product_polynomials_with_witness(polys, witness):
    mul_ = lambda x, y: x * y
    sum_ = lambda x, y: x + y
    return reduce(sum_, map(mul_, polys, witness))

# no of variables = 7 = no of columns
# no of equations = 4 = no of rows
n, m = 4, 7
L = np.array([[0, 0, 1, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 0],
              [0, 0, 0, -5, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 1]])
R = np.array([[0, 0, 1, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 0], 
              [0, 0, 0, 1, 0, 0, 0], 
              [0, 0, 0, 0, 1, 0, 0]])
O = np.array([[0, 0, 0, 0, 1, 0, 0], 
              [0, 0, 0, 0, 0, 1, 0], 
              [0, 0, 0, 0, 0, 0, 1], 
              [0, 1, 0, 0, 0, -1, 0]])

# let x = 4, y = -2
x = 4
y = -2

v1 = x**2
v2 = v1*v1
v3 = -5*y*y
out = x**4 - 5*y**2*x**2

w = [1, out, x, y, v1, v2, v3]

# witness = GF(matrix_modulo(w))
witness = GF([(k % GF.order + GF.order) % GF.order for k in w])
L_galois, R_galois, O_galois = [GF(matrix_modulo(matrix)) for matrix in [L, R, O]]
assert np.equal(np.multiply(L_galois.dot(witness), R_galois.dot(witness)), O_galois.dot(witness)).all(), "result contains inequality"

# these contain a list of polynomials that each column of the matrix will be transformed into
U_polys = np.apply_along_axis(interpolate_column, 0, L_galois)
V_polys = np.apply_along_axis(interpolate_column, 0, R_galois)
W_polys = np.apply_along_axis(interpolate_column, 0, O_galois)
# we have 4 no of rows so each column will have 4 elements which will correspond to a polynomial
# which will form a polynomial matrix of degree n-1 which will have a total of n co-efficients
xs = GF(np.array([i for i in range(1, n+1)]))

# these matrices will contain the coefficients of the polynomials
L_poly, R_poly, O_poly = [np.empty((n,m), dtype=np.int64) for _ in range(3)]
for j in range(m):
    l_col, r_col, o_col = GF(L_galois[:, j]), GF(R_galois[:, j]), GF(O_galois[:, j]) 
    l_poly, r_poly, o_poly = galois.lagrange_poly(xs, l_col).coefficients(), galois.lagrange_poly(xs, r_col).coefficients(), galois.lagrange_poly(xs, o_col).coefficients()
    l_poly = handle_coefficient(l_poly)
    r_poly = handle_coefficient(r_poly)
    o_poly = handle_coefficient(o_poly)
    L_poly[:, j] = l_poly
    R_poly[:, j] = r_poly
    O_poly[:, j] = o_poly
    
L_poly, R_poly, O_poly = L_poly.astype(np.int64), R_poly.astype(np.int64), O_poly.astype(np.int64)

'''Each of the terms is taking the inner product of the witness with the column-interpolating polynomials. 
That is, each of summation terms are effectively the inner product between <1, a₁, …, aₘ> and <u₀(x), u₁(x), ..., uₘ(x)>'''
term_1 = inner_product_polynomials_with_witness(U_polys, witness)
term_2 = inner_product_polynomials_with_witness(V_polys, witness)
term_3 = inner_product_polynomials_with_witness(W_polys, witness)

# adding the right hand side of the eqn so that we match the degree of the polynomials on both sides
# add lhs to h*t where t is of degree 4 which has roots at 1, 2, 3, 4 and h i computed by the formula:h= (U*V - W)/t
# note that it is eventually a identity in its vector form 

# the purpose for two different poynomials instead of one is to make sure the prover knows the witness vector

# t = (x - 1)(x - 2)(x - 3)(x - 4)
t = galois.Poly([1, 78], field = GF) * galois.Poly([1, 77], field = GF) * galois.Poly([1, 76], field = GF) * galois.Poly([1, 75], field = GF)

h = (term_1 * term_2 - term_3) // t

assert term_1 * term_2 == term_3 + h * t, "division has a remainder"