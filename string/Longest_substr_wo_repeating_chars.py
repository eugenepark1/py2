'''
Created on Sep 27, 2017

@author: eugenep

given a string, find the length of the longest substring w/o repeating chars

given 'abcabcb' -> 'abc' 3
given 'bbbbbb' -> 'b' 1
given 'pwwkew' -> 'wke' 3
'''


def find_longest_substr(input):
    
    max_subchar = ""

    tmp = {}
    cur_subchar = ""
    for ch in input:

        if ch not in tmp:
            #print "%s: not in tmp" % ch
            tmp[ch] = 1
            cur_subchar += ch
        else: # repeated
            #print "%s: already in tmp" % ch
            if len(cur_subchar) > len(max_subchar):
                max_subchar = cur_subchar
            cur_subchar = ch
            tmp = {ch: 1}
                
    return max_subchar

print find_longest_substr("abcabcb")
print find_longest_substr("pwwkew")
print find_longest_substr("bbbbbb")
            
            