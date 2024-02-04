from py_ecc.bn128 import add, multiply, G1, neg, eq

# Example: 39 = x^3 -4*x^2 + 3x - 2

# prover
x = 5
out = x**3 - 4*x**2 + 3*x - 1 
# encrpting x, x^2, x^3 separately
x_enc = multiply(G1, x)
x2_enc = multiply(G1, x*x)
x3_enc = multiply(G1, x**3)

# verifier

lhs = multiply(G1, 39)
rhs = add(add(add(multiply(x3_enc, 1), neg(multiply(x2_enc, 4))), multiply(x_enc, 3)), neg(multiply(G1, 1)))

assert eq(lhs, rhs) , "result contains inequality"  