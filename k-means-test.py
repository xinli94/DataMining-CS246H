#!/usr/bin/env python
import numpy as np
import pickle

with open ('centroid', 'rb') as f1:
    centroid_list = pickle.load(f1)
##print centroid_list

with open ('pt', 'rb') as f2:
    pt_list = pickle.load(f2)

centroid_target = [[-51.85, -88.72],[-88.72, -2.38],[-2.38, 17.21],[-25.82, -94.42]]
for item in centroid_target:
    flag = 0
    print 'find centroid:  ' + str(item)
    for c in centroid_list:
        if np.absolute(c[0]-item[0])<0.01 and np.absolute(c[1]-item[1])<0.01:
            flag = 1
            break
    print '  ', flag==1

outliner_target = [[-129.63, -121.72],[75.51, 155.71],[-8.08, -161.19],[-100.79, 153.81]]
ans = np.inf
ans_val = 0
for i,item in enumerate(outliner_target):
    minval = np.inf
    for c in centroid_list:
        tmp = (item[0]-c[0])**2 + (item[1]-c[1])**2
        if tmp < minval:
            minval = tmp
    print minval
    if minval > ans_val:
        ans_val = minval
        ans = i
print
print 'outlier detection:  ' + str(outliner_target[ans])
        



