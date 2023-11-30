# Avoid cache
import sys
sys.dont_write_bytecode = True

import free_twopac as ftp
import projbar_loc as projbar
import gen_points as gp
import generates_example as ge
import numpy as np
import time

dir = [0.7, 0.3]
ge.generates_file()

#load the examples
path_to_random = "data_random.txt"
path_to_sphere = "data_sphere.txt"
path_to_torus = "data_torus.txt"

# load the files
pts_r , grd_r = ge.read_file(path_to_random)
pts_s , grd_s = ge.read_file(path_to_sphere)
pts_t , grd_t = ge.read_file(path_to_torus)

# Run 2pac
# Hacky fix for 2pac
from silencer import stdout_redirected
import os
with stdout_redirected(to=os.devnull):
    
    bd_r = []
    bd_t = []
    bd_s = []
    perf_tp_r = []
    perf_tp_s = []
    perf_tp_t = []

    for i in range(0,3):
        before_tp = time.perf_counter()
        bd_r.append(ftp.func_rips_hom_free_res(pts_r,grd_r,i))
        after_tp = time.perf_counter()
        perf_tp_r.append(after_tp - before_tp)
        before_tp = time.perf_counter()
        bd_s.append(ftp.func_rips_hom_free_res(pts_s,grd_s,i))
        after_tp = time.perf_counter()
        perf_tp_s.append(after_tp - before_tp)
        before_tp = time.perf_counter()
        bd_t.append(ftp.func_rips_hom_free_res(pts_t,grd_t,i)) 
        after_tp = time.perf_counter()
        perf_tp_t.append(after_tp - before_tp)
    
#end of hacky fix

print("=== Perf 2pac ===")
print("-- random points --")
for x in perf_tp_r: print(x, "s")
print("-- sphere points --")
for x in perf_tp_s: print(x, "s")
print("-- torus points --")
for x in perf_tp_t: print(x, "s")
print("")

#=========== PBT ============================

st_r = []
st_s = []
st_t = []

pbt_r = []
pbt_s = []
pbt_t = []

perf_pbt_r = []
perf_pbt_s = []
perf_pbt_t = []

for bd in bd_r:
    before_st = time.perf_counter()
    st_r.append(projbar.stratif(bd))
    pbt_r.append(projbar.pbt_from_stratif(bd, st_r[-1]))
    after_st = time.perf_counter()
    perf_pbt_r.append(after_st - before_st)

for bd in bd_s:
    before_st = time.perf_counter()
    st_s.append(projbar.stratif(bd))
    pbt_s.append(projbar.pbt_from_stratif(bd, st_s[-1]))
    after_st = time.perf_counter()
    perf_pbt_s.append(after_st - before_st)

for bd in bd_t:
    before_st = time.perf_counter()
    st_t.append(projbar.stratif(bd))
    pbt_t.append(projbar.pbt_from_stratif(bd, st_t[-1]))
    after_st = time.perf_counter()
    perf_pbt_t.append(after_st - before_st)


print("=== Perf projected barcode template ===")
print("-- random points --")
for x in perf_pbt_r: print(x, "s")
print("-- sphere points --")
for x in perf_pbt_s: print(x, "s")
print("-- torus points --")
for x in perf_pbt_t: print(x, "s")
print("")

# =========== Info PBT ==================

nb_gen_r = [len(x) for x in bd_r]
nb_gen_s = [len(x) for x in bd_s]
nb_gen_t = [len(x) for x in bd_t]

nb_st_r = [len(x) for x in st_r]
nb_st_s = [len(x) for x in st_s]
nb_st_t = [len(x) for x in st_t]

print("===  Number generators ===")
print("-- random points --")
for x in nb_gen_r: print(x)
print("-- sphere points --")
for x in nb_gen_s: print(x)
print("-- torus points --")
for x in nb_gen_t: print(x)
print("")

print("===  Number cells ===")
print("-- random points --")
for x in nb_st_r: print(x)
print("-- sphere points --")
for x in nb_st_s: print(x)
print("-- torus points --")
for x in nb_st_t: print(x)
print("")

# ================ Pairs ================

pairs_r = []
pairs_s = []
pairs_t = []

perf_pairs_r = []
perf_pairs_s = []
perf_pairs_t = []

for i in range(3):
    before_pairs = time.perf_counter()
    pairs_r.append((projbar.query_from_pbt(dir, pbt_r[i], st_r[i], bd_r[i])))
    after_pairs = time.perf_counter()
    perf_pairs_r.append(after_pairs - before_pairs)

    before_pairs = time.perf_counter()
    pairs_s.append((projbar.query_from_pbt(dir, pbt_s[i], st_s[i], bd_s[i])))
    after_pairs = time.perf_counter()
    perf_pairs_s.append(after_pairs - before_pairs)

    before_pairs = time.perf_counter()
    pairs_t.append((projbar.query_from_pbt(dir, pbt_t[i], st_t[i], bd_t[i])))
    after_pairs = time.perf_counter()
    perf_pairs_t.append(after_pairs - before_pairs)

print("=== Perf queries ===")
print("-- random points --")
for x in perf_pairs_r: print(x, "s")
print("-- sphere points --")
for x in perf_pairs_s: print(x, "s")
print("-- torus points --")
for x in perf_pairs_t: print(x, "s")
print("")