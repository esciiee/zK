from libnum import has_sqrtmod_prime_power, sqrtmod_prime_power

def y_squared(x, mod):
    return (x**3 + 3) % mod

prime = 11

for x in range(prime):
    ysquared = y_squared(x, prime)
    if has_sqrtmod_prime_power(ysquared, prime, 1):
        square_root = sqrtmod_prime_power(ysquared, prime, 1)
        for sr in square_root:
            print(f'x = {x}, y = {sr}')
