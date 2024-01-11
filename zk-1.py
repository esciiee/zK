# exercise: to prove knowledge of a solution to a linear system of equations
# le the problem be 23x=161
# the prover claims to know a x for which ax+by=c
# the verifier has to agree on the formula and perform calculation to verify the provers statement


from py_ecc.bn128 import G1, add, multiply, eq


# takes a, b, c as inputs which are the coefficients of the linear equation ax+by=c and x, y which satisfies the equation
def proof(a, b, c, secret_x, secret_y):
    x = multiply(G1, secret_x*a)
    y = multiply(G1, secret_y*b)
    return verifier(c, x, y)


def verifier(c, x, y):
    if eq(add(x,y), multiply(G1, c)):
        return "The Statement is True"
    return "The Statement is False"


print(proof(3, 2, 10, 2, 2))
