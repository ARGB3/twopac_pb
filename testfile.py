# Avoid cache
import sys
sys.dont_write_bytecode = True

import free_twopac as ftp
import projbar_loc as projbar
import numpy as np
import time

pts, grd = ftp.random_pts_grds(500,2)
dir = [0.7, 0.3]

# Hacky fix for 2pac
from silencer import stdout_redirected
import os
with stdout_redirected(to=os.devnull):
    before_tp = time.perf_counter()
    bd = ftp.func_rips_hom_free_res(pts,grd,1)
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