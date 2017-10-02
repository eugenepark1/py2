'''
Created on Oct 1, 2017

@author: eugene

given an array and a value, remove all instance of that value in place and return the new length

given [3,2,2,3] val=3
return 2 with first two elements being 2
'''


def remove_val(arr, val):
    
    slow_ptr = 0
    for i,n in enumerate(arr):
        if n != val:
            arr[slow_ptr] = n
            slow_ptr += 1
    return slow_ptr

arr = [3,2,2,3]
print remove_val(arr, 3)