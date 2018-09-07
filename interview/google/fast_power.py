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



def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
def calculate_fast_power_recursion(x,y, odd=False):
    print "cnt"
    is_odd = odd
    if not odd: # no need to evaluate if already decided that it's odd
        if not is_even(y):
            is_odd = True
            y = y -1
    
    if y <= 1:
        return x
    else:
        return calculate_fast_power_recursion(x, y/2, is_odd) **2


def calculate_fast_power_brute(x,y):
    '''
    O(y)
    '''
    
    cur = 1
    op_cnt = 0
    for i in range(y):
        op_cnt += 1
        cur *= x
    print "op_cnt: %s " % op_cnt
    return cur

def calculate_fast_power_half(x,y):
    '''
    O(y) 2*2*2*2*2*2*2*2
    O(log y)
            2*8
         2*4         ^2
       2*2           ^2
     2*1             ^2
    '''
    
    even = True
    if not is_even(y):
        y -= 1
        even = False
    
    exp = y
    powered = x
    op_cnt = 0
    while True:
        op_cnt += 1
        if exp == 1:
            break
        else:
            exp = exp/2
            powered = powered **2
    
    print "op_cnt: %s " % op_cnt
    if not even:
        return powered * x
    else:
        return powered

print calculate_fast_power_brute(2,16)
print calculate_fast_power_half(2,16)
print calculate_fast_power_recursion(2,16)