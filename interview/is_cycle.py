'''
Created on Aug 24, 2018

@author: eugene

Determine whether a circular array of relative indices is a single complete cycle

returns True if:
    1. start == end
    2. every index is visited
    3. only wraps around once
'''


def is_cycle(arr):

    visited = set()
    pos = 0
    for step in range(len(arr)):
        pos = (pos + arr[pos]) % len(arr)
        if pos in visited:
            return False
        else: 
            visited.add(pos)

    return pos == 0
    


circular_array = [2, 2, -1]

'''
(0) (1) (2)

(0) --> (2) --> (1) --> (0)
    start == end
    every index is visited
    only wraps around once
'''
print is_cycle(circular_array)