# %%
from py_ecc.bn128 import G1, multiply, add, eq, neg
import matplotlib.pyplot as plt
import numpy as np
import math

xs = []
ys = []

for i in range(1, 5):
    xs.append(i)
    ys.append(int(multiply(G1, i)[1]))
    xs.append(i)
    ys.append(int(neg(multiply(G1, i))[1]))

plt.scatter(xs, ys, marker='.')


# %%
