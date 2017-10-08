'''
Created on Oct 7, 2017

@author: eugene

find the contiguous subarray within an array (containing at least one number) which has the largest sum

given [-2,1,-3,4,-1,2,1,-5,4]
output [4,-1,2,1]
'''

def maxSubArray(arr):
    if len(arr) == 0:
        raise Exception("Array empty") # should be non-empty
      
    runSum = maxSum = arr[0]
    i = 0
    start = finish = 0

    for j in range(1, len(arr)):

        if arr[j] > (runSum + arr[j]):
            runSum = arr[j]
            i = j
        else:
            runSum += arr[j]

        if runSum > maxSum:
            maxSum = runSum
            start = i
            finish = j
            
    print "maxSum =>", maxSum
    print "start =>", start, "; finish =>", finish

arr = [-2,1,-3,4,-1,2,1,-5,4]
maxSubArray(arr)