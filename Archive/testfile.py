import free_twopac as ftp
import projbar_loc as projbar

pts, grd = ftp.random_pts_grds(17,2)
m0, m1 = ftp.free_hom_RC(pts,grd,1)
print("========= Here starts =========")
m0_rgrd = m0.row_grades
m0_cgrd = m0.column_grades
m0_clm = m0.columns

m1_rgrd = m1.row_grades
m1_cgrd = m1.column_grades
m1_clm = m1.columns
'''
print("==== m0 ======")
print("rgrd")
for x in m0_rgrd : print(x)
print("cgrd")
for x in m0_cgrd : print(x)
print("clm")
for x in m0_clm : print(x)

print("==== m1 ======")
print("rgrd")
for x in m1_rgrd : print(x)
print("cgrd")
for x in m1_cgrd : print(x)
print("clm")
for x in m1_clm : print(x)
'''
bd = []
for x in m0_rgrd:
    bd.append([0,x,[]])
for i in range(len(m0_cgrd)):
    bd.append([-1,m0_cgrd[i],m0_clm[i]])
for i in range(len(m1_cgrd)):
    bd.append([-2,m1_cgrd[i],[x + len(m0_rgrd) for x in m1_clm[i]]])
    #bd.append([-2,m1_cgrd[i],[x for x in m1_clm[i]]])

'''
print("Boundary matrix:")
for i in range(len(bd)): print(i, bd[i])
print("")
'''
pairs = projbar.projected_perspairs(bd, [0.5,0.5])

for pair in pairs: 
    print(pair) 
    if len(pairs) == 0 : print("No persistence pairs")