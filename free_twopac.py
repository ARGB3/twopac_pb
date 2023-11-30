from twopac import FunctionRipsComplex

import numpy as np
import matplotlib.pyplot as plt

def random_pts_grds(nbpts, dimension):
    points = np.floor(np.random.rand(nbpts, dimension)*10)
    grades = np.floor(np.random.rand(nbpts)*10)
    return points, grades

def func_rips_hom_free_res(pts,grds, dghom):
    dists  = np.linalg.norm(pts[:,None,:] - pts[None,:,:], axis=-1)
    cpx = FunctionRipsComplex(grds, dists)
    homology = cpx.sfd().Chunk(dghom+1).Homology(dghom)

    # Hacky fix,
    # TBM when the 2pac python binding are fixed
    it_hom = iter(homology)
    n = [0]*(dghom+1)
    for i in range(len(n)):
        n[i] = next(it_hom) 
    #end of hacky fix

    m0_rgrd = n[dghom][0].row_grades
    m0_cgrd = n[dghom][0].column_grades
    m0_clm = n[dghom][0].columns

    m1_rgrd = n[dghom][1].row_grades
    m1_cgrd = n[dghom][1].column_grades
    m1_clm = n[dghom][1].columns

    bd = []
    for x in m0_rgrd:
        bd.append([0,x,[]])
    for i in range(len(m0_cgrd)):
        bd.append([-1,m0_cgrd[i],m0_clm[i]])
    for i in range(len(m1_cgrd)):
        bd.append([-2,m1_cgrd[i],[x + len(m0_rgrd) for x in m1_clm[i]]])
    
    return bd

def print_points(pts,grds):
    fig, ax = plt.subplots()
    ax.scatter(pts[:, 0],pts[:,1], c = grds)
    plt.show()

