#!/usr/bin/env python

idx_now = 0
wdict = {}
idxdict = {}
with open('browsing.txt','r') as f:
    for line in f:
        for w in line.split():
            if wdict.get(w) == None:
                idx_now += 1
                wdict[w] = idx_now

            idx = wdict[w]
            if idxdict.get(idx) == None:
                idxdict[idx] = 1
            else:
                idxdict[idx] += 1
            print idxdict[idx]


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


