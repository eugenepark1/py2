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
            break
        
    return result

assert is_palin("aabaa") is True


# find all palins in a word

def find_all_palins(word):
    found_palins = []
    for i in range(len(word)):
        for j in range(len(word), -1, -1):
            if is_palin(word[i:j]):
                found_palins.append(word[i:j])
    
    return found_palins

print find_all_palins('abababa')
# O(n)


#find longest palindromic substring 
# easy solution: find all and get max