'''
Created on Oct 1, 2017

@author: eugene

given a sorted array and a target value, return the index if the target is found
if not, return the index where it would be if it were inserted in order

[1,3,5,6]    5? 2
[1,3,5,6]    0? 0
[1,3,5,6]    7? 4
[1,3,5,6]    2? 1
'''

def return_index(arr, val):
    '''
        if val exists in arr, return index
        elif current element in array is bigger than val, return index
    '''
    for i, n in enumerate(arr):
        if n >= val:
            return i
    
    return len(arr) # made it out w/o finding it so index should be the last



arr = [1,3,5,6]
print return_index(arr, 5)
print return_index(arr, 0)
print return_index(arr, 7)
print return_index(arr, 2)

