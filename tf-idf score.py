#!/usr/bin/env python
import os
import math

rootDir = 'C:\Users\LX\Desktop\Shakespeare'
file_name = 'KING_HENRY_THE_EIGHTH'
target = 'fiddle'
tar_cnt = 0
word_cnt = 0
path = os.path.join(rootDir, file_name)
with open(path) as f:
    for line in f:
        for w in line.split():
            word_cnt = word_cnt+1
            if w == target:
                tar_cnt = tar_cnt+1
tf = float(tar_cnt)
##print tf

file_cnt = 0
file_num = 0
for file in os.listdir(rootDir):
    path = os.path.join(rootDir, file)
    with open(path) as f:
        file_num = file_num+1
        cnt = 0
        for line in f:
            for w in line.split():
                if w == target:
                    cnt = cnt+1
        if cnt>0:
            file_cnt = file_cnt+1
idf = math.log(float(math.fabs(file_num))/file_cnt)
##print idf
print tf*idf
                    

