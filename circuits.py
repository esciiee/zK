field_size = 29

# Example: Proving b is the inverse of a

## prover
def compute_inv(a):
    return pow(a, -1, field_size)

a = 22
b = compute_inv(a)

## verifier
### the verifier doesnt compute the inverse, it just checks that a*b = 1
assert (a * b) % field_size == 1