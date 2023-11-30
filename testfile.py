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
'''
bd = [[0, (3.1622776601683795, 9.0), []],
       [0, (3.605551275463989, 6.0), []],
        [-1, (4.0, 9.0), [1, 0]],
        [-1, (4.123105625617661, 6.0), [1]]]
'''

st = projbar.stratif(bd)
pairs = projbar.pbt_from_stratif(bd, st)
for pair in pairs: print(pair)

'''
bd_new, conv_on, conv_no = projbar.sorted_bd_from_dir(bd, dir)

print("bd_new")
for b in bd_new: print(b)
pairs_new = projbar.pp_from_srt_bd(bd_new, conv_on, conv_no)

print("new pairs")
for pair in pairs_new: 
    print(pair) 
    if len(pairs_new) == 0 : print("No persistence pairs")
'''