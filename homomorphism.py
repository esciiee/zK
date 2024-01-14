from py_ecc.bn128 import curve_order, G1, multiply, add, eq, neg, field_modulus
from random import randint

# ------------------------------- Elliptic Curve Addtion ------------------------------- #

# mutiplying any point with the curve order will result in the same point
x = randint(1, curve_order)
y = randint(1, curve_order)
assert eq(multiply(G1, x), multiply(G1, x+curve_order))

# assert eq(multiply(G1, x), multiply(G1, x+field_modulus)
#           ), "Field modulus is not curve order, it is a modulo over which the curve is defined"

# also note that since we get the same point when we multiply any point with the curve order
# then we can imply that G1 times (x+y)mod(order) = G1 times x + G1 times y
assert eq(multiply(G1, (x+y) % curve_order),
          add(multiply(G1, x), multiply(G1, y % curve_order)))

# ------------------------------- Encoding Rational Numbers ------------------------------- #

# we can encode rational numbers as points on the curve
# for example 1/3 can be written as 1*multiplicative inverse of 3 mod curve order
# 1/3 = 1*3^-1 mod curve order and 1/3+8/3 = 3
mul_inv = pow(3, -1, curve_order)
# print("1/3 can be written as 1*multiplicative inverse of 2 mod curve order", pow(3, -1, curve_order) % curve_order)
# print("similarly 8/3 can be written as 5*multiplicative inverse of 2 mod curve order", (8*pow(3, -1, curve_order)) % curve_order)
# adding assertion to check if the above statement is true
assert eq(add(multiply(G1, 1*mul_inv),multiply(G1, 8*mul_inv)), multiply(G1, 3))

# ------------------------------- Associativity ------------------------------- #

a= randint(1, curve_order)
b= randint(1, curve_order)
c= randint(1, curve_order)

# (a+b)+c = a+(b+c)
lhs = add(add(multiply(G1, a), multiply(G1, b)), multiply(G1, c))
rhs = add(multiply(G1, a), add(multiply(G1, b), multiply(G1, c)))
assert eq(lhs, rhs)

# -------------------------------- ECDSA malleability -----------------------------#

# the property simpley says that mul(G1, (order-x)) = neg(mul(G1,x))

x = randint(1, curve_order)
assert multiply(G1, (curve_order-x)), neg(multiply(G1, x))

# also recall that the value of the x remains the same when the inverse happens only the y value changes
assert multiply(G1, x)[0], neg(multiply(G1,x))[0]

# also note that there are points whose inverse is the point itself inv(A) = A
# for these points if double them we get inv(A) op A = I, we get point of identity which is obvious