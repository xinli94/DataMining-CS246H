#!/usr/bin/env python
import os

rootDir = 'C:\Users\LX\Desktop\Shakespeare'
file = 'THE_TRAGEDY_OF_OTHELLO_MOOR_OF_VENICE'
target = 'beard'
ans = 0
path = os.path.join(rootDir, file)
with open(path) as f:
    for line in f:
        for w in line.split():
            if w == target:
                ans = ans+1
print ans
                    
