'''
Created on Oct 9, 2017

@author: eugenep

a cool string is a string where each char has the name number of counts
or where one and only one can be removed  
'''


def cool_string(input_str):
    
    countMap = {}
    for ch in input_str:
        if not ch in countMap:
            countMap[ch] = 0
        countMap[ch] += 1
    
    freqMap = {}
    for ch, cnt in countMap.iteritems():
        if cnt not in freqMap:
            freqMap[cnt] = []
        freqMap[cnt].append(ch)