# Avoid cache
import sys
sys.dont_write_bytecode = True

import free_twopac as ftp
import projbar_loc as projbar

import numpy as np

pts, grd = ftp.random_pts_grds(100,2)
dir = [0.7, 0.3]

# Hacky fix for 2pac
from silencer import stdout_redirected
import os
with stdout_redirected(to=os.devnull):
    bd = ftp.func_rips_hom_free_res(pts,grd,1)
#end of hacky fix


st = projbar.stratif(bd)
pbt = projbar.pbt_from_stratif(bd, st)
pairs = projbar.query_from_pbt(dir, pbt, st, bd)

print("BARS")
for pair in pairs : print(pair)