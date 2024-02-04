from py_ecc.bn128 import curve_order, add, multiply, G1, Z1, eq
import galois
from functools import reduce

# polynomials over finite fields
# Z1 is point at infinity aka identity element
# G1 is the generator point

GF = galois.GF(curve_order)
def inner_product(ec_points, coefficients):
    return reduce(add, (multiply(point, int(coefficient)) for point, coefficient in zip(ec_points, coefficients)), Z1)

def gen_points_powers_of_tau(k, degree):
    return [multiply(G1, k**i) for i in range(degree+1)]

# p = (x-9)*(x-10)
p = galois.Poly([1, -9], field=GF)*galois.Poly([1, -10], field=GF)

# let the secret number be 13
tau = GF(13)
points = gen_points_powers_of_tau(int(tau), p.degree)
eval = p(tau)
eval_point = multiply(G1, int(eval))

eval_ecc = inner_product(points, p.coeffs[::-1])

if(eq(eval_point, eval_ecc)):
    print("the polynomial evaluation is correct")


