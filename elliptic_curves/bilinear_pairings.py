from py_ecc.bn128 import G1, G2, add, multiply, eq, neg, pairing


# ------------------------------- Multi-Dimensional Elliptic Curve Points ----------------------------

# multi dimensional points like ((p,q),(r,s)) will behave similar to what we saw in case of (x,y)
assert eq(add(add(G2, G2), G2), multiply(G2, 3))

# ------------------------------- e(aG1, bG2) = e(G1, abG2) = e(abG1, G2) ------------------
a = 5
b = 6
c = 30
A = multiply(G2, a)
B = multiply(G1, b)
C = multiply(G1, c)
assert eq(pairing(A,B), pairing(G2, C))
# print(pairing(A,B))
# use google colloab if this is not working locally
# --------------------------------- example problem ---------------------------------------

a = 4
b = 3
c = 6
d = 2

# -ab + cd = 0

# the verifier formula: A1B2 + C1D2 = e(-aG1, bG2) + e(cG1, dG2)

# A1 = neg(aG1))
A1 = neg(multiply(G1, a))
B2 = multiply(G2, b)
C1 = multiply(G1, c)
D2 = multiply(G2, d)
print(f'{A1[0]}\n{A1[1]}\n{B2[0]}\n{B2[1]}\n{C1[0]}\n{C1[1]}\n{D2[0]}\n{D2[1]}')
# Now we have the values encrypted into points on G1 and G2 groups, 
# someone else or a program can confirm that we computed A1B2+C1D2=0 
# correctly without knowing the individual values of a, b, c, or d. 