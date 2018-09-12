'''
Created on Aug 31, 2017

@author: eugene

when there is an inner and outer loop, ask if you need to shoten the inner loop (i.e. possible palins)
'''

# 1st inner-outer loop
# 2nd is have all the palins in dictionary and search against it o(1)
# cigar tragic
# palin means reveserd is the same

def is_palin(first_word, second_word):
    concat_word = first_word + second_word
    if concat_word == concat_word.reversed():
        return True
    return False

def give_possible_palins(word):
    'tragic'
    return

# 1) store english_dict in Dictionary
#   * lookup will be O(1))

# runtime is O(N*K*1) where N is the number of words in english_dict, K is the number of possible palins and lookup
# Pseudo
# for word in english_dict:
#   for possible in give_possible_palins(word)
#       if possible in english_dict:
#           add possible

def check_palin(word):
    for i in xrange(len(word)/2):
        if word[i] != word[-1*(i+1)]:
            return False
    return True

def all_palindromes(string):

    left,right=0,len(string)
    j=right
    results=[]

    while left < right-1:
        temp = string[left:j] #Time complexity O(k)
        j-=1

        if check_palin(temp):
            results.append(temp)

        if j<left+2:
            left+=1
            j=right

    return list(set(results))

print all_palindromes("racecarenterelephantmalayalam")