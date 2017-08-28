'''
Created on Aug 27, 2017

@author: eugene
'''

'''
hash table: maps keys to values for highly efficient lookup
one implementation is array of linked list and a hash cod fucntion
the keys hash code could be an int or long
if collision is high O(N) where N is the number of keys or lookup can be O(1)
you can also implment this in balanced binary search tree which would give O(log N) lookup time

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
    