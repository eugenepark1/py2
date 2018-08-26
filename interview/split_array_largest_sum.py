'''
Created on Aug 24, 2018

@author: eugene

Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays. 
Write an algorithm to minimize the largest sum among these m subarrays.

Note:
If n is the length of array, assume the following constraints are satisfied:

1 ¡Â n ¡Â 1000
1 ¡Â m ¡Â min(50, n)

Input:
nums = [7,2,5,10,8]
m = 2

Output:
18

Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
'''


def splitArray(nums, m):
    """
    :type nums: List[int]
    :type m: int
    :rtype: int
  
      Q1) how do we come up with these permutations?
    [7] [2,5,10,8]       7 25           1 4
    [7,2] [5,10,8]       9 23           2 3
    [7,2,5] [10,8]       14 18          3 2
    [7,2,5,10] [8]       24 8           4 1
    
    [7] [2] [5,10,8]
    [7] [2,5] [10,8]
    [7] [2,5,10] [8]
    
    [7,2] [5] [10,8]
    [7,2] [5,10] [8]
  
    [7,2,5] [10] [8]
    """
    
    
    while True:
        
    
    
nums = [7,2,5,10,8]
m = 2
print splitArray(nums, m)