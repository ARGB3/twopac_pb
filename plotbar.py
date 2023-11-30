import numpy as np
import matplotlib.pyplot as plt
path_bar = "bars_r_0.txt"

f = open("bars/bars_t_2.txt", "r")
lines = f.readlines()
f.close()

bars = []

for line in lines:
    pair = line.split()
    bars.append(np.array([float(pair[0]), float(pair[1])]))

bars = np.array(bars)
m = max(bars[:,0])
n = max(bars[:,1])
mn = max(m,n)

plt.scatter(bars[:,0], bars[:,1], s=10)
plt.xlim(0, mn)
plt.ylim(0, mn)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()