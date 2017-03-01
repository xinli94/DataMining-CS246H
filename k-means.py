#!/usr/bin/env python
import numpy as np
import pickle

init_list = [];
init_path = 'initial'
with open(init_path) as f1:
    for line in f1:
        tmp_list = []
        for w in line.split():
            tmp_list.append(w)
        init_list.append( [float(tmp_list[0][1:-1]),float(tmp_list[1][0:-1])] )
init_cnt = len(init_list)
##init_array = np.asarray(init_list)
##print init_list
##print init_array

pt_list = [];
pt_path = 'points'
with open(pt_path) as f2:
    for line in f2:
        tmp_list = []
        for w in line.split():
            tmp_list.append(w)
        pt_list.append( [float(tmp_list[0][1:-1]),float(tmp_list[1][0:-1])] )
pt_cnt = len(pt_list)
##pt_array = np.asarray(pt_list)
##print pt_list

for itr in range(1,11):
    c_list = []
    for i, pt in enumerate(pt_list):
        minval = np.inf
        c = np.inf
        for j, init in enumerate(init_list):
            tmp = (pt[0]-init[0])**2 + (pt[1]-init[1])**2
            if tmp < minval:
                minval = tmp
                c = j
        c_list.append(c)
##        print c
                
    for j, init in enumerate(init_list):
        u_tmp = [0,0];
        l_tmp = 0;
        for i, pt in enumerate(pt_list):
            if c_list[i] == j:
                l_tmp = l_tmp+1
                u_tmp[0] = u_tmp[0]+pt[0]
                u_tmp[1] = u_tmp[1]+pt[1]
        init_list[j][0] = u_tmp[0]/l_tmp
        init_list[j][1] = u_tmp[1]/l_tmp

with open('centroid', 'wb') as f3:
    pickle.dump(init_list, f3)

with open('pt', 'wb') as f4:
    pickle.dump(pt_list, f4)

##file_centroid = open('centroid', 'w')
##for item in init_list:
##    file_centroid.write("%s\n" % item)
##
##file_pt = open('pt', 'w')
##for item in pt_list:
##    file_pt.write("%s\n" % item)
            


