#!/usr/bin/env python
import os

rootDir = 'C:\Users\LX\Desktop\Shakespeare'
target = 'knave'
ans = 0
for file in os.listdir(rootDir):
    path = os.path.join(rootDir, file)
    with open(path) as f:
        cnt = 0
        for line in f:
            for w in line.split():
                if w == target:
                    cnt = cnt+1
        if cnt>0:
            ans = ans+1
print ans
                    
