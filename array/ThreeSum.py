'''
Created on Sep 27, 2017

@author: eugenep

given an array of S of n integers, are there elements, a, b, c in S such that a + b + c = 0?
Fine all unique triplets in the array which gives the sum of zero

Note: solution must not contain duplicate triplets

given [-1, 0, 1, 2, -1, -4]

solution is [
    [-1, 0, 1]
    [-1, -1, 2]
]
'''
def ThreeSum(arr):
    solution_set = []
    for i, n in enumerate(arr):
        for j, m in enumerate(arr):
            if i == j:
                continue
            for k,o in enumerate(arr):
                if k == i or k == j:
                    continue
                
                    if n + m + o == 0:
                        solution_set.append( [i, j, k] )
    return solution_set

arr = [-1, 0 , 1, 2, -1, -4]

print ThreeSum(arr)

