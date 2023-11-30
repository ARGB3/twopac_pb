# Avoid cache
import sys
sys.dont_write_bytecode = True

import free_twopac as ftp
import projbar_loc as projbar
import gen_points as gp
import numpy as np
import time


dir = [0.7, 0.3]

# Generates random points
pts_r, grd_r = ftp.random_pts_grds(200,3)
# Generate points on the torus with some outliers
pts_t , grd_t = gp.gen_torus(200, 20, plot = True)
# Generate points on the torus with some outliers
pts_s , grd_s = gp.gen_sphere(200, 20, plot = True)

# Hacky fix for 2pac
from silencer import stdout_redirected
import os
with stdout_redirected(to=os.devnull):
    before_tp = time.perf_counter()
    bd = ftp.func_rips_hom_free_res(pts_s,grd_s,2)
    after_tp = time.perf_counter()
#end of hacky fix

print("Perf twopac", (after_tp - before_tp) * 1000)

before_pbt = time.perf_counter()
st = projbar.stratif(bd)
pbt = projbar.pbt_from_stratif(bd, st)
after_pbt = time.perf_counter()
print("Perf pbt", (after_pbt - before_pbt) * 1000)

before_query = time.perf_counter()
pairs = projbar.query_from_pbt(dir, pbt, st, bd)
after_query = time.perf_counter()
print("Perf query", (after_query - before_query) * 1000)

'''
print("BARS")
for pair in pairs : print(pair)
'''