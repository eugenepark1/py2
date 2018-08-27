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
  
     n=5
     m=2
  
    1) come up with these permutations
    [7] [2,5,10,8]       7 25           1 4
    [7,2] [5,10,8]       9 23           2 3
    [7,2,5] [10,8]       14 18          3 2
    [7,2,5,10] [8]       24 8           4 1
    
    
    n=5
    m=3
    
    [7] [2] [5,10,8]                     1 1 3
    [7] [2,5] [10,8]                     1 2 2
    [7] [2,5,10] [8]                     1 3 1
    
    [7,2] [5] [10,8]                     2 1 2
    [7,2] [5,10] [8]                     2 2 1
  
    [7,2,5] [10] [8]                     3 1 1
    """
    
    def perm(m, n):
        if m == 1:  # base case
            return [(n,)]
        perms = []
        for s in range(1, n):  # combine possible start values: 1 through n-1 ...
            for p in perm(m-1, n-s):  # ... with all appropriate smaller perms 
                perms.append((s,) + p)
        return perms
    
    def generate_permutations(m, n):
        all = []
        cur = [0 for i in range(m)]
        len_perm = m*2
        while True:
            for i in range(m):
                if cur[i] == 0:
                    if i != m-1:
                        cur[i] = 1
                    else:
                        cur[i] = n-m
            
            all.append(cur)
            if len(all) >= len_perm:
                break
        return all
    
    '''
    n = len(arr)
    m=2
    1 n-(m-1)
    ...
    n-(m-1) 1
    
    m=3
    1 1 n-(m-1)
    ...
    n-(m-1) 1 1
    
    1, 2, ... m
    
    split_permutations = []
    cur_m_buckets = [0 for i in range(m)]
    while True:
        # init
        for i in range(cur_m_buckets):
            if i == m-1:
                
            else:
                cur_m_buckets[i] = 1
            
            
        split_permutations.append(cur_m_buckets)
    ''' 
            
            
            
    
    
nums = [7,2,5,10,8]
m = 2
print splitArray(nums, m)