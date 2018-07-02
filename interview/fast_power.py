'''
Created on Jul 2, 2018

@author: eugene

Calculate fast power better than O(y) where solution is x^y 
'''


def calculate_fast_power_brute(x,y):
    '''
    O(y)
    '''
    cur = x
    for i in range(y):
        cur *= x
    
    return cur

for i in range(10):
    print calculate_fast_power_brute(2, i)