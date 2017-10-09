'''
Created on Sep 27, 2017

@author: eugenep

Given an array of integers, return indices of the two numbers such that they add up to a specific target

Example:

given nums = [2, 7, 11, 15], target 9

return [0, 1] where num[0] + num[1] = 2 + 7 = 9


'''
def TwoSum(arr, tgt):
    # O(N^2)
    for i,n in enumerate(arr):
        for j,m in enumerate(arr):
            if i == j:
                continue # same index so skip
            else:
                if n + m == tgt:
                    return [i, j]
                
    return None

def TwoSum_dict(arr, tgt):
    # O(N + N + N + 1)
    tmp_dict = dict( zip(arr, [i for i,n in enumerate(arr)]) )
    for i, n in enumerate(arr):
        look_for = tgt - n
        if look_for in tmp_dict:
            return [i, tmp_dict[look_for]]

    return None

arr = [2, 7, 11, 15]
tgt = 9

print TwoSum(arr, tgt)
print TwoSum_dict(arr, tgt)

