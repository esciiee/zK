import numpy as np
from py_ecc.bn128 import G1, G2, add, multiply, eq, neg, pairing

# --------------------------------- out = 3*x*x*y + 5*x*y -x - 2y + 3 ---------------------------------

# A naive method for generating zero knowledge proofs for the above equation

# caution: this is not an efficient method for generating zkp and requires a lot of computation 

# method: encrypting  the witness vector by multiplying with G1 and G2 points
# then generating bilinear pairings for the encrypted points
# mathematically: e(aG1, bG2) = e(G1, abG2) = e(abG1, G2)

# prover
# Claim : "I know the value of x and y for which out = 14"

# inputs
x = 1
y = 2

# outputs
out = 3*x*x*y + 5*x*y -x - 2*y + 3

# auxiliary inputs
v1 = 3*x*x
v2 = 5*x*y

# defining the matrices for which Ls . Rs = Os
# L: LHT according to the constraints
# R: RHT according to the constraints
# O: the output matrix of the constraints  
# s: witness matrix which needs to be encrypted to hide the values of x and y 

L = np.array([[0, 0, 3, 0, 0, 0], [0, 0, 5, 0, 0, 0], [0, 0, 0, 0, 1, 0]])
R = np.array([[0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 1, 0, 0]])
O = np.array([[0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1], [-3, 1, 1, 2, 0, -1]])

# witness vector
w = np.array([1, out, x, y, v1, v2])

# sG1: the encrypted witness vector in G1 group
wg1 = np.array([multiply(G1, i) for i in w])
wg2 = np.array([multiply(G2, i) for i in w])


# verifier
def verify(L, R, O, wg1, wg2):
    # Ls: the encrypted LHT
    for k in range(len(L)):
        suml = multiply(wg1[0], L[k][0])
        sumr = multiply(wg2[0], R[k][0])
        sumo = multiply(wg1[0], O[k][0])
        for i in range(1,len(L[0])):
            suml = add(suml, multiply(wg1[i], L[k][i]))
            sumr = add(sumr, multiply(wg2[i], R[k][i]))
            sumo = add(sumo, multiply(wg1[i], O[k][i]))
        if(pairing(sumr, suml) != pairing(G2, sumo)):
            return False
    return True

# e(Ls, Rs) = e(Os, G2)
print(verify(L, R, O, wg1, wg2))