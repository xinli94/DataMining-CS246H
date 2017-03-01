#!/usr/bin/env python
import operator
import itertools
from collections import OrderedDict

S = 100
idx_now = 0
cnt_now = 0
wdict = {}
idxdict = {}
basdict = {}
with open('browsing.txt','r') as f:
    for line in f:
        list_bas = []
        for w in line.split():
            ##name -> idx
            if wdict.get(w) == None:
                idx_now += 1
                wdict[w] = idx_now
                list_bas.append(idx_now)
            else:
                list_bas.append(wdict.get(w))
            ##count the occurrences of each item
            idx = wdict[w]
            if idxdict.get(idx) == None:
                idxdict[idx] = 1
            else:
                idxdict[idx] += 1
        ##create baskets
        cnt_now += 1
        basdict[cnt_now] = list_bas
##print wdict
##print idxdict
##print basdict

##find frequent items
freq_item_dict = {key:value for key,value\
                  in idxdict.items() if value > S-1}
##print 'items: ', len(freq_item_dict)
##print freq_item_dict

##find frequent pairs
freq_pair_dict = {}
for idx in basdict:
    basket = basdict[idx]
    basket = [value for value in basket if freq_item_dict.get(value) != None]
    candidate = list(itertools.permutations(basket,2))
    for item in candidate:
        if freq_pair_dict.get(item) != None:
            freq_pair_dict[item] += 1
##            freq_pair_dict[(item[1],item[0])] += 1
        else:
            freq_pair_dict[item] = 1
##            freq_pair_dict[(item[1],item[0])] = 1

##print 'frequent pairs: ', len(freq_pair_dict)

freq_pair_dict = {key:value for key,value \
                  in freq_pair_dict.items() if value > S-1}

freq_pair_dict = OrderedDict(sorted(freq_pair_dict.items(),\
                               key=operator.itemgetter(1),reverse=True))
##print 'frequent pairs: ', len(freq_pair_dict)
##print freq_pair_dict

##sort dictionary in decending order    
pair_confidence_dict = {key:(float(value)/freq_item_dict[key[0]]) \
                        for key,value in freq_pair_dict.items()}

pair_confidence_dict = sorted(pair_confidence_dict.items(),\
                               key=operator.itemgetter(1),reverse=True)
##print pair_confidence_dict

print ""
print "answer to (2.d)"
cnt = 0
for pair in pair_confidence_dict:
    tup = pair[0]
    print "pairs of items: ", wdict.keys()[wdict.values().index(tup[0])],\
          "implies", wdict.keys()[wdict.values().index(tup[1])]
    print "confidence: ", pair[1]
    cnt += 1
    if cnt == 5:
        break


##find frequent triples
freq_trip_dict = {}
for idx in basdict:
    basket = basdict[idx]
    basket = [value for value in basket if freq_item_dict.get(value) != None]
    candidate = list(itertools.permutations(basket,3))
    for item in candidate:
        if freq_pair_dict.get((item[0],item[1])) != None \
           and freq_pair_dict.get((item[0],item[2])) != None \
           and freq_pair_dict.get((item[2],item[1])) != None:
            if freq_trip_dict.get(item) != None:
                freq_trip_dict[item] += 1
    ##            freq_pair_dict[(item[0],item[2],item[1])] += 1
            else:
                freq_trip_dict[item] = 1
    ##            freq_pair_dict[(item[1],item[0])] = 1
##print len(freq_trip_dict)

freq_trip_dict = {key:value for key,value \
                  in freq_trip_dict.items() if value > S-1}
freq_trip_dict_tmp = {}
for item in freq_trip_dict:
    if freq_trip_dict_tmp.get(item) == None\
       and freq_trip_dict_tmp.get((item[1],item[0],item[2])) == None:
        freq_trip_dict_tmp[item] = freq_trip_dict[item]
freq_trip_dict = freq_trip_dict_tmp

freq_trip_dict = OrderedDict(sorted(freq_trip_dict.items(),\
                               key=operator.itemgetter(1),reverse=True))
##print len(freq_trip_dict)
##print freq_trip_dict

##sort dictionary in decending order    
trip_confidence_dict = {key:(float(value)/freq_pair_dict[(key[0],key[1])]) \
                        for key,value in freq_trip_dict.items()}

trip_confidence_dict = OrderedDict(sorted(trip_confidence_dict.items(),\
                               key=operator.itemgetter(1),reverse=True))
##print trip_confidence_dict

trip_confidence_dict_tmp = {}
for trip in trip_confidence_dict:
    if trip_confidence_dict[trip] == 1:
        trip_confidence_dict_tmp[trip] = trip_confidence_dict[trip]

trip_confidence_dict = {}
for trip in trip_confidence_dict_tmp:
    trip_confidence_dict[(wdict.keys()[wdict.values().index(trip[0])],\
                          wdict.keys()[wdict.values().index(trip[1])],\
                          wdict.keys()[wdict.values().index(trip[2])])] = 1
##print trip_confidence_dict

trip_confidence_dict = OrderedDict(sorted(trip_confidence_dict.items(),\
                               key=operator.itemgetter(0)))

##print trip_confidence_dict

print ""
print "answer to (2.e)"
cnt = 0
for trip in trip_confidence_dict:
    tup = trip
    print "triples of items: ", (tup[0],\
          tup[1]), "implies", \
          tup[2]
    print "confidence: 1" 
    cnt += 1
    if cnt == 5:
        break





    
##print wdict['FRO40251']
##print freq_item_dict[wdict['FRO40251']]
##print sorted_freq_pair_dict





##sorted_freq_pair_dict = sorted_freq_pair_dict.reverse()
##print sorted_freq_pair_dict
##for idx in freq_pair_dict:
##    if freq_pair_dict[idx] < 100:
##        del freq_pair_dict[idx]
##                    print freq_pair_dict

                
##            
##        if freq_item_dict[item]


##with open('browsing.txt','r') as f:
##    for line in f:
##        for w in line.split():
##            idx = wdict[w]
##            if idxdict.get(idx) == None:
##                idxdict[idx] = 1
##            else:
##                idxdict[idx] += 1


##print wdict                
                
##print wlist

##wfreq = []
##wlist_new = []
##w = 0 
##for w_next in wlist:
##    if w_next != w:
##        w = w_next
##        cnt = wlist.count(w)
##        if cnt>1000:
##            wfreq.append(wlist.count(w))
##            wlist_new.append(w)
##            print w, ': ', wlist.count(w)
##wfreq = [wlist.count(w) for w in wlist]
##print wfreq





    
##wdict = dict(zip(wlist, wfreq))
####print wdict

##wdictNew = dict()
##for w in wdict:
##    if wdict[w]>100:
##        wdictNew[w] = wdict[w]
####print wdictNew

##w = sorted([(wdict[key],key) for key in wdict])
##w.reverse()
##print w


