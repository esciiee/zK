from py_ecc.bn128 import multiply, G2, G1, curve_order
from functools import reduce
import galois

def gen_points_powers_of_tau(k, degree, curve):
    if curve == 2:
        return [multiply(G2, k**i) for i in range(degree+1)]
    return [multiply(G1, k**i) for i in range(degree+1)]

def gen_points_powers_of_tau_t(k, degree, t):
    return [multiply(G1, (k**i)*t) for i in range(degree+1)]

def polynomial_with_roots(degree, field):
    # Generate a polynomial with roots at 1, 2, 3, ..., degree
    return reduce(lambda x, y: x * galois.Poly([1, -y], field), range(1, degree + 1))

export = { polynomial_with_roots, 
          gen_points_powers_of_tau,
          gen_points_powers_of_tau_t } 