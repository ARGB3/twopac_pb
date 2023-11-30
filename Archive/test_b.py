from twopac import *

import numpy as np
import matplotlib.pyplot as plt

N = 3
points = np.random.rand(N, 2)
grades = np.random.rand(N) 
dists  = np.linalg.norm(points[:,None,:] - points[None,:,:], axis=-1)

points = points * 10.
points = np.floor(points)

grades = np.floor(grades*10)

fig, ax = plt.subplots()
ax.scatter(points[:, 0],points[:,1], c = grades)
#plt.show()

cpx = FunctionRipsComplex(grades, dists)
homology = cpx.sfd().Chunk(0).Homology(0)
print(dir(homology))
m =  next(homology.__iter__())
print(m[0].row_grades)
'''
for m in homology.__iter__():
    for i in range(len(m)):
        print("Degree ", i)
        print("Row grades")
        print(m[i].row_grades)
        print("Column grades")
        print(m[i].column_grades)
        print("Columns")
        print(m[i].columns)
'''