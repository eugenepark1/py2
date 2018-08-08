'''
Created on Aug 7, 2018

@author: eugenep

Given an array, find the maximum possible sum in a subarray where
    subarray is a contiguous subsequence in an array.

arr: 2 -1 2 3 4 -5
ans: 2+-1+2+3+4 == 10


-1    
(e)
(s)  
-1    1     2


(e)
(s)
-1

(s)  (e)
-1    1

     (s)   (e)
-1    1     2


if you add the cur_val and sum increases, then move (e)


'''

def find_maxSum(arr):
    '''
    continuous: there is some start index and an end index
    as iterate through an array, need to make a decision on moving either of those indices
    when to move start index?
        if cur, cur-1, and cur-2 < 0
    
    when to move end index?
    
    move (e), then move (s)
    '''
    
    start_index = 0
    end_index = 0
    curSum = 0
    maxSum = 0
    for cur_index, value in enumerate(arr):
        if cur_index == 0:
            curSum = value
            maxSum = value
        else:
            curSum += value
            if curSum > maxSum:
                end_index = cur_index
                


    return (start_index, end_index)

# you cant make the decision to move (s) to index 3 until you are there and look at index 2 and 1
# you cant move (e) unless curSum > maxSum
testArr = [2,-5,3,4,5]
print find_maxSum(testArr)

print find_maxSum([-1, 1, 2])