#!/usr/bin/env python
import operator
import itertools
from collections import OrderedDict

rdict = {}
keydict = {}
valuedict = {}
key_cnt = 0
value_cnt = 0
with open('epa-http.txt') as f:
    for line in f:
        rlist = []
        for w in line.split():
            rlist.append(w)
        if keydict.get(rlist[0]) == None:
            key_cnt += 1
            keydict[rlist[0]] = key_cnt
        str_tmp = ''.join(rlist[2:-2])
        if valuedict.get(str_tmp) == None:
            value_cnt += 1
            valuedict[str_tmp] = value_cnt
        key = (keydict[rlist[0]],valuedict[str_tmp])
        if rdict.get(key) == None:
            rdict[key] = 1
        else:
            rdict[key] += 1
##        rdict[keydict[rlist[0]]] = valuedict[str_tmp]

##print keydict
##print rdict

rdict_all = {}
for item in rdict:
    if rdict_all.get(item[0]) == None:
        rdict_all[item[0]] = 1#rdict[item]
    else:
        rdict_all[item[0]] += 1#rdict[item]
##print rdict_all
    
rdict_all = sorted(rdict_all.items(),\
                               key=operator.itemgetter(1),reverse=True)

##print rdict_all

##print rdict
output = {}
cnt = 0
for item in rdict_all:
    request = keydict.keys()[keydict.values().index(item[0])]
    if output.get(request) == None:
        cnt += 1
        output[request] = 1
        print request, item[1]
    else:
        output[request] += 1
    if cnt == 20:
        break

    

##cnt_unique_request_dict = {}
##for key,value in rdict:
##    item = (key, value)
##    print item
##    if cnt_unique_request_dict.get(item) == None:
##        cnt_unique_request_dict[item] = 1
##    else:
##        cnt_unique_request_dict[item] += 1
##print cnt_unique_request_dict[item]
