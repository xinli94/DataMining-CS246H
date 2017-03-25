#!/usr/bin/env python
import numpy as np
import pickle
import operator
import itertools

states = 'DC,WA,AL,CO'
area = '480,681,307,602'
years = '57,51,66,45'
names = 'MICHAEL JONES,JOHN SMITH,JAMES SMITH,ROBERT SMITH'

with open('customer_data','rb') as f1:
    d = pickle.load(f1)

states_dict = {}
area_dict = {}
year_dict = {}
name_dict = {}
for idx in d:
    [name,state,phone,gender,year,bill] = d[idx]
    if name_dict.get(name) != None:
        name_dict[name] += bill
    else:
        name_dict[name] = bill
    
    flag = 0
    if gender == 'F':
        flag = 1
    if states_dict.get(state) != None:
        states_dict[state] = [x+y for x,y in zip(states_dict[state],[flag,1])]
    else:
        states_dict[state] = [flag,1]
    
    area_tmp = phone[0:3]
    if area_dict.get(area_tmp) != None:
        area_dict[area_tmp] += 1
    else:
        area_dict[area_tmp] = 1

    if year_dict.get(year) != None:
        year_dict[year] += 1
    else:
        year_dict[year] = 1
    

for item in states.split(','):
    tmp = states_dict[item]
    if float(tmp[0])/tmp[1] >= 0.5:
        print item
print

for item in area.split(','):
    tmp = area_dict[item]
    print (int(item),tmp)
print

tmp = sorted(year_dict.items(), key=operator.itemgetter(1),reverse=True)
for y in tmp[0:10]:
    for item in years.split(','):
        if '19'+item == y[0]:
            print item
print

for item in names.split(','):
    tmp = '{0:.2f}'.format(name_dict[item])
    print (item,tmp)
print
