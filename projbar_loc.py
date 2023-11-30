## Projected barcode
# Computes the projected barcode from a boundary matrix

#================ Modules ============================
import numpy as np
import phat

#================ Functions ============================
def projected_perspairs(boundary, direction):
    #projection
    proj_indented_boundary = [ [boundary[i][0], np.dot(boundary[i][1],direction), boundary[i][2],i] 
                              for i in range(len(boundary)) ]

    '''
    print("Proj_intended_bd")
    for i in range(len(proj_indented_boundary)): print(i, proj_indented_boundary[i])
    print("")
    '''
    
    #sorting
    proj_indented_boundary = sorted(proj_indented_boundary, key=lambda item: (item[1], -item[0]))
    
    #Conversion table
    conv_table = {proj_indented_boundary[i][-1] : i
                  for i in range(len(proj_indented_boundary))}
    '''
    print("Proj_intended_bd_SORTED")
    for i in range(len(proj_indented_boundary)): print(i, proj_indented_boundary[i])
    print("")
    print("conv_table")
    for x in conv_table : print(x,conv_table[x])
    print("")
    '''

    #phat_boundary
    phat_boundary = [(-x[0], sorted([conv_table[i] for i in x[2]])) for x in proj_indented_boundary]
    #print("length p_bd", len(phat_boundary))

    '''
    print("Phat_boundary")
    for i in range(len(phat_boundary)): print(i, " ", phat_boundary[i])
    print("") 
    '''

    #call phat
    phat_boundary_matrix = phat.boundary_matrix(representation =
                                                 phat.representations.vector_vector)
    phat_boundary_matrix.columns = phat_boundary
    
    phat_pairs = phat_boundary_matrix.compute_persistence_pairs()

    print("pairs")
    for x in phat_pairs: 
        print(x)
        if x[0]>x[1]: print("PROBLEM")
    print("")
    
    #Translate phat output
    perspairs_new = [(proj_indented_boundary[x[0]][1], proj_indented_boundary[x[1]][1]) 
                     for x in phat_pairs 
                     if proj_indented_boundary[x[0]][1] != proj_indented_boundary[x[1]][1]]
    return perspairs_new

def stratif(bd):
    gnrts = [np.array(x[1]) for x in bd]
    #for x in gnrts: print(x)
    stratif = set()
    for i in range(len(gnrts)):
        for j in range(i+1,len(gnrts)):
            g = gnrts[i] - gnrts[j]
            if g[0]*g[1] < 0:
                if g[0] > 0: h = np.array([g[1],-g[0]])
                if g[0] < 0: h = np.array([-g[1],g[0]])
                ph = h[1]/(h[0]+h[1]) 
                stratif.add(ph)
    
    return sorted(list(stratif))

def sorted_bd_from_dir(bd,dir):
    srt_bd = [ [bd[i][0], np.dot(bd[i][1],dir), bd[i][2], i] for i in range(len(bd)) ]
    srt_bd = sorted(srt_bd, key=lambda item: (item[1], -item[0]))
    cv_table_on = {srt_bd[i][-1] : i for i in range(len(srt_bd))}
    cv_table_no = {i : srt_bd[i][-1] for i in range(len(srt_bd))}
    for i in range(len(srt_bd)):
        (srt_bd[i])[1] = i
        srt_bd[i].pop()
    
    return srt_bd, cv_table_on, cv_table_no

def pp_from_srt_bd(srt_bd, cv_table_on, cv_table_no):
    phat_boundary = [(-x[0], sorted([cv_table_on[i] for i in x[2]])) for x in srt_bd]

    #call phat
    phat_boundary_matrix = phat.boundary_matrix(representation =
                                                 phat.representations.vector_vector)
    phat_boundary_matrix.columns = phat_boundary
    phat_pairs = phat_boundary_matrix.compute_persistence_pairs()

    #Transform pairs with the non-sorted bd indices
    pp = [(cv_table_no[x[0]], cv_table_no[x[1]]) for x in phat_pairs ]
    return pp

def pbt_from_stratif(bd, st):
    if len(st) == 0: return []

    pairs = []
    proj_dir = [1 - np.mean([0,st[0]]), np.mean([0,st[0]])]
    srt_bd, cv_tb_on, cv_tb_no = sorted_bd_from_dir(bd,proj_dir)
    pairs.append(pp_from_srt_bd(srt_bd,cv_tb_on, cv_tb_no))
    
    if len(st) > 2:
        for i in range(1,len(st)-1):
            proj_dir = [1 - np.mean([st[i],st[i+1]]), np.mean([st[i],st[i+1]])]
            srt_bd, cv_tb_on, cv_tb_no = sorted_bd_from_dir(bd,proj_dir)
            pairs.append(pp_from_srt_bd(srt_bd,cv_tb_on, cv_tb_no))

    if len(st) > 1:
        proj_dir = [1 - np.mean([1,st[-1]]), np.mean([1,st[-1]])]
        srt_bd, cv_tb_on, cv_tb_no = sorted_bd_from_dir(bd,proj_dir)
        pairs.append(pp_from_srt_bd(srt_bd,cv_tb_on, cv_tb_no))
    return pairs
