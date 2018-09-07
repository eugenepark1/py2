'''
Created on Sep 6, 2018

@author: eugenep
'''


arr = [1, 3, 5, 8, 10, 15]

def bin_search(tgt, arr):
    if len(arr) == 1:
        if arr[0] == tgt:
            return 0
        else:
            return -1
    
    mid = len(arr)/2
    if arr[mid] == tgt:
        return mid
    else:
        if arr[mid] > tgt:
            return bin_search(tgt, arr[:mid])
        else:
            return bin_search(tgt, arr[mid:])
    
print bin_search(15, arr)