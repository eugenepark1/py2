'''
Created on Oct 1, 2017

@author: eugene

given a sorted array, remove the duplicates in place such that each element appear only once and return the new length

do not allocate extra space for another array

given [1,1,2]
return 2
'''

def get_removed_length(sorted_arr):
    slow_ptr = None
    
    for i,n in enumerate(sorted_arr):
        if slow_ptr is None:
            slow_ptr = i
        elif n != sorted_arr[slow_ptr]:
            slow_ptr += 1
            sorted_arr[slow_ptr] = n

    return slow_ptr + 1

sorted_arr = [1,1,2]
print get_removed_length(sorted_arr)