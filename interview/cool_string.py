'''
Created on Oct 9, 2017

@author: eugenep

a cool string is a string where each char has the name number of counts
or where one and only one can be removed  
'''


def cool_string(input_str):
    
    if input_str == "":
        return False
    
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
        
    
    '''
    aaabbbc
    
    aaabbbcc
    aaabbbcccc
    
    '''
        
    if len(freqMap) == 1:
        return True
    elif len(freqMap) >= 3:
        return False
    else:
        freqMap_sorted = {}
        freqMap_sorted['big'] = {}
        freqMap_sorted['small'] = {}
        
        for k,v in freqMap.iteritems():
            if len(freqMap_sorted['big']) == 0:
                freqMap_sorted['big']['cnt'] = k
                freqMap_sorted['big']['chr_arr'] = v
            else:
                if k > freqMap_sorted['big']['cnt']:
                    freqMap_sorted['small']['cnt'] = freqMap_sorted['big']['cnt']
                    freqMap_sorted['small']['chr_arr'] = freqMap_sorted['big']['chr_arr']
                    freqMap_sorted['big']['cnt'] = k
                    freqMap_sorted['big']['chr_arr'] = v
                else:
                    freqMap_sorted['small']['cnt'] = k
                    freqMap_sorted['small']['chr_arr'] = v
                    
        
        '''
        aaabbbc - okay

        aaabbbcc  - not okay
        aaabbbcccc - okay
        '''         
        if freqMap_sorted['small']['cnt'] == 1 and len(freqMap_sorted['small']['chr_arr']) == 1:
            return True
        elif (freqMap_sorted['big']['cnt'] - freqMap_sorted['small']['cnt'] == 1) and len(freqMap_sorted['big']['chr_arr']) == 1:
            return True

        return False
    
assert cool_string('aaabbbc') is True
assert cool_string('aaabbbcccc') is True
assert cool_string('aaabbbcc') is False
    
    