'''
Created on Jul 2, 2018

@author: eugene

Calculate fast power better than O(y) where solution is x^y 
'''

def power(base, exp):
    """ Fast power calculation using repeated squaring """
    if exp < 0:
        return 1 / power(base, -exp)
    ans = 1
    while exp:
        if exp & 1:
            ans *= base
        exp >>= 1
        base *= base
    return ans

def calculate_fast_power_brute(x,y):
    '''
    O(y)
    '''
    cur = x
    for i in range(y):
        cur *= x
    
    return cur

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
def calculate_fast_power_recursion(x,y, odd=False):
    is_odd = odd
    if not odd: # no need to evaluate if already decided that it's odd
        if not is_even(y):
            is_odd = True
            y = y -1
    
    if y <= 1:
        if is_odd:
            return x^2
        else:
            return x
    else:
        return calculate_fast_power_recursion(x, y/2, is_odd) * x

def calculate_fast_power_half(x,y):
    '''
    O(y)
    '''
    cur = x
    for i in range(y):
        cur *= x
    
    return cur


for i in range(10):
    print calculate_fast_power_half(2, i)