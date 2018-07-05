'''
Created on Jul 5, 2018

@author: eugenep

check if given number is a prime
A prime number is a natural number greater than 1 that cannot be formed by multiplying two smaller natural numbers. 
A natural number greater than 1 that is not prime is called a composite number.

is_square
122
    1**2
    2**2
    3**2
    ...
    12**2  --> can stop here as 144 > 122
    
is_prime

'''


def is_square(x):
    index = 1
    while True:
        squared = index **2
        if x == squared:
            return True
        
        if squared > x:
            return False
        
        index += 1

print is_square(121)


def is_prime(x):
    '''
    trial division: check whether any prime integer m from 2 to sqrt(n) evenly divides n (the division leaves no remainder). 
    11
    2 6 = 12
    3 4 = 12
    
    17
    2 9 = 18
    3 6 = 18
    4 5 = 20
    '''
    return
