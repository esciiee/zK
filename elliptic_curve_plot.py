#%%
import libnum
import matplotlib.pyplot as plt

#code to generate plot of an elliptic curve points from the eqn y^2 = x^3 + 3(mod 11)
#y^2 = x^3 + 3(mod 11)

def generate_points(mod): 
    xs = []
    ys = []

    def y_squared(x):
        return (x**3 + 3) % mod
    
    for x in range(mod):
        ysquared = y_squared(x)
        if libnum.has_sqrtmod_prime_power(ysquared, mod, 1):
            square_root = libnum.sqrtmod_prime_power(ysquared, mod, 1)
            for sr in square_root:
                xs.append(x)
                ys.append(sr)
    return xs, ys

p=1000
xs, ys = generate_points(p)
fig, (ax1) = plt.subplots(1, 1)
fig.suptitle('y^2 = x^3 + 3(mod 11)')
fig.set_size_inches(10, 10)
plt.grid()
plt.scatter(xs, ys)
# %%
