'''
Created on Aug 27, 2017

@author: eugene
'''

'''
you have a list of words given
'''


HASHMAP_KEY = {}

def calc_hash(word):
    dict_word = {}
    for ch in word:
        if not ch in dict_word:
            dict_word[ch] = 0
        dict_word[ch] += 1
        
    #return hash(dict_word)
    return hash(word)

    #ord('c')
    #hashfunc=numberofitemstablesize=numberofitemstablesize. 
    #(44%11==044%11==0).

def create_dict(words):
    global HASHMAP_KEY
    for word in words:
        key_value = calc_hash(word)
        HASHMAP_KEY[key_value] = word
    