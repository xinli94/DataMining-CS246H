#!/usr/bin/env python
import numpy as np
import pickle

d = {}
with open('customer.tsv','r') as f1:
    for line in f1:
        w = line.split()
        if len(w[-2]) == 2:
            dev = 2
            year = w[-1]
        else:
            dev = 0
            year = '19' + w[-1][-2:]
        idx = w[0]
        name = ' '.join(w[1:3])
        gender = w[-2-dev].upper()
        state = w[-5-dev].upper()
        phone = ''.join([s for s in w[-3-dev] if s.isdigit()])
        d[idx] = [name,state,phone,gender,year]
##        print name,state,phone,gender,year

with open('billing.tsv', 'r') as f2:
    for line in f2:
        w = line.split()
        if len(d[w[0]]) == 5:
            d[w[0]].extend([float(w[1])])
        else:
            d[w[0]][-1] += float(w[1])
        print d[w[0]]

with open('customer_data', 'wb') as g1:
    pickle.dump(d, g1)        




