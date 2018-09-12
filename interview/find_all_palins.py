'''
Created on Sep 9, 2018

@author: eugene
'''

def is_palin(word):
    result = True
    mid = len(word)/2
    for i in range(mid):
        if word[i] != word[len(word)-1-i]:
            result = False 
        
    return result

assert is_palin("aabaa") is True