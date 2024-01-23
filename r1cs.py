import numpy as np
from random import randint

# Example 1: z = x*y

# define the matrices
C = np.array([[0, 1, 0, 0]])
A = np.array([[0, 0, 1, 0]])
B = np.array([[0, 0, 0, 1]])

# witness vector
witness = [1, 4223, 41, 103]

# Multiplication is element-wise(dot product), not matrix multiplication.
# Result contains a bool indicating an element-wise indicator that the equality is true for that element.
result = C.dot(witness) == A.dot(witness) * B.dot(witness)

# check that every element-wise equality is true
assert result.all(), "result contains an inequality"

# Example 2: z = x*y*z*u

# to construct matrices A, B, C such that C . witness = A . witness * B . witness
# eqaulity constraint- 1: v1 = x*y
# equality constraint- 2: v2 = z*u
# equality constraint- 3: z = v1*v2
# LHT: for constructing A Matrix: x, z, v1
# RHT: for constructing B Matrix: y, u, v2
# Result: for constructing C Matrix: z, v1, v2

# the matricec construction is done as follows:
# each item in the matrix represent if the variables corresponding to the column is present in the witness matrix equation
# corresponding to the row and its value is the coefficient of the variable in the equation

# define the matrices

A = np.array([[0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 1, 0]])
B = np.array([[0, 0, 0, 1, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 1]])
C = np.array([[0, 0, 0, 0, 0, 0, 1, 0],
              [0, 0, 0, 0, 0, 0, 0, 1],
              [0, 1, 0, 0, 0, 0, 0, 0]])

x = randint(1, 1000)
y = randint(1, 1000)
z = randint(1, 1000)
u = randint(1, 1000)

out = x*y*z*u
v1 = x*y
v2 = z*u

w = np.array([1, out, x, y, z, u, v1, v2])

result = C.dot(w) == np.multiply(A.dot(w), B.dot(w))

assert result.all(), "result contains an inequality"

# Example 3: Addition with a constant: out = x*y + z

# addition is free in snarks, why ?
# because the dot product sums up the elemnet any ways ---> (out - z) = x*y

# w: [1, out, x, y]
# LHT: for constructing A Matrix: x : [0, 0, 1, 0]
# RHT: for constructing B Matrix: y : [0, 0, 0, 1]
# Result: for constructing C Matrix: out - z : [-z, 1, 0, 0]

x = randint(1, 1000)
y = randint(1, 1000)
z = randint(1, 1000)

out = x*y + z

# define the matrices

A = np.array([[0, 0, 1, 0]])
B = np.array([[0, 0, 0, 1]])
C = np.array([[-z, 1, 0, 0]])

w = np.array([1, out, x, y])

result = C.dot(w) == np.multiply(A.dot(w), B.dot(w))

assert result.all(), "result contains an inequality"

# Example 4: Multiplication with a constant: out = 2*x*x + y

# out = 2x*x + y; y is a constant and addition is free so we dont need to add y to the witness vector
# w: [1, out, x]
# matrices consist of rows equal to no of equations and columns equal to no of variables in the witness vector
# here consider that LHT is x whose coefficient is 2 and RHT is x whose coefficient is 1
# LHT: for constructing A Matrix: x : [[0, 0, 2]]
# RHT: for constructing B Matrix: v1 : [[0, 0, 1]]
# Result: for constructing C Matrix: out : [[-y, 1, 0]]

x = randint(1, 1000)
y = randint(1, 1000)

out = 2*x*x + y

# define the matrices

A = np.array([[0, 0, 2]])
B = np.array([[0, 0, 1]])
C = np.array([[-y, 1, 0]])

w = np.array([1, out, x])

result = C.dot(w) == np.multiply(A.dot(w), B.dot(w))

assert result.all(), "result contains an inequality"

# Example 5: out = 3*x*x*y + 5*x*y -x - 2y + 3

# eqaulity constraint- 1: v1 = 3x*x
# equality constraint- 2: v2 =   5x*y
# equality constraint- 3: out -v2 + x + 2y -3 = v1*y
# w = [1, out, x, y, v1, v2]
# LHT: for constructing A Matrix: x, y, v1: [[0, 0, 3, 0, 0, 0], [0, 0, 5, 0, 0, 0], [0, 0, 0, 0, 1, 0]]
# RHT: for constructing B Matrix: x, y, v2: [[0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1]]    
# Result: for constructing C Matrix: out -v2 + x + 2y -3 : [[0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1], [-3, 1, 1, 2, 0, -1]]

x = randint(1, 1000)
y = randint(1, 1000)
v1 = 3*x*x
v2 = 5*x*y
out = 3*x*x*y + 5*x*y -x - 2*y + 3

# define the matrices

A = np.array([[0, 0, 3, 0, 0, 0], [0, 0, 5, 0, 0, 0], [0, 0, 0, 0, 1, 0]])
B = np.array([[0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 1, 0, 0]])
C = np.array([[0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1], [-3, 1, 1, 2, 0, -1]])

w = np.array([1, out, x, y, v1, v2])

result = C.dot(w) == np.multiply(A.dot(w), B.dot(w))

assert result.all(), "result contains an inequality"