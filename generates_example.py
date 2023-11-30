# Avoid cache
import sys
sys.dont_write_bytecode = True

import free_twopac as ftp
import projbar_loc as projbar
import gen_points as gp
import numpy as np
import time

def read_file(path):
    pts = []
    grd = []
    f = open(path)
    lines = f.readlines()
    index_grades = -1 
    for i in range(len(lines)):
        if lines[i] == "Grades\n": 
            index_grades = i+1
            break
        if lines[i] != "Points\n" and lines[i] != "\n" :
            pt = lines[i].split("\n")[0]
            pt = pt.split()
            pts.append(np.array([float(pt[0]),float(pt[1]),float(pt[2])]))
    for i in range(index_grades, len(lines)):
        grd.append(float(lines[i]))
    f.close()
    return np.array(pts), np.array(grd)

def generates_file():
    # Generates points and grades
    pts_r, grd_r = ftp.random_pts_grds(100,3)
    pts_t , grd_t = gp.gen_torus(100, 20, plot = True)
    pts_s , grd_s = gp.gen_sphere(100, 20, plot = True)

    # Save the files
    f = open("data_random.txt", "w")
    f.write("Points\n")
    for pt in pts_r: f.write(str(pt[0])+ " " + str(pt[1]) + " " + str(pt[2]) + '\n')
    f.write("\nGrades\n")
    for g in grd_r: f.write(str(g) + '\n') 
    f.close()

    f = open("data_sphere.txt", "w")
    f.write("Points\n")
    for pt in pts_s: f.write(str(pt[0])+ " " + str(pt[1]) + " " + str(pt[2]) + '\n')
    f.write("\nGrades\n")
    for g in grd_s: f.write(str(g) + '\n') 
    f.close()

    f = open("data_torus.txt", "w")
    f.write("Points\n")
    for pt in pts_t: f.write(str(pt[0])+ " " + str(pt[1]) + " " + str(pt[2]) + '\n')
    f.write("\nGrades\n")
    for g in grd_t: f.write(str(g) + '\n') 
    f.close()
