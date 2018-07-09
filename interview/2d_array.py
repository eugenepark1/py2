'''
Created on Jul 5, 2018

@author: eugene

Given a  2D Array, :
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0

We define an hourglass in A to be a subset of values with indices falling in this pattern in 's graphical representation:
a b c
  d
e f g

There are 16 hourglasses in arr, and an hourglass sum is the sum of an hourglass' values. Calculate the hourglass sum for every hourglass in arr, then print the maximum hourglass sum.

For example, given the 2D array:
-9 -9 -9  1 1 1 
 0 -9  0  4 3 2
-9 -9 -9  1 2 3
 0  0  8  6 6 0
 0  0  0 -2 0 0
 0  0  1  2 4 0
 
 We calculate the following 16 hourglass values:
 -63, -34, -9, 12, 
-10, 0, 28, 23, 
-27, -11, -2, 10, 
9, 17, 25, 18

Complete the function hourglassSum in the editor below. It should return an integer, the maximum hourglass sum in the array.

hourglassSum has the following parameter(s):

arr: an array of integers

Input Format

Each of the 6 lines of inputs arr[i] contains 6 space-separated integers arr[i][j].

Output Format

Print the largest (maximum) hourglass sum found in arr.

Complete the function hourglassSum in the editor below. It should return an integer, the maximum hourglass sum in the array.

hourglassSum has the following parameter(s):

arr: an array of integers
'''
arr = [[] for i in range(6)]

arr[5] = [-9, -9, -9,  1, 1, 1 ]
arr[4] = [  0, -9, 0 , 4, 3, 2]
arr[3] = [ -9 ,-9, -9,  1, 2, 3]
arr[2] = [  0 , 0 , 8,  6 ,6 ,0]
arr[1] = [ 0,  0,  0, -2, 0 ,0]
arr[0] = [ 0,  0,  1,  2, 4, 0]


# Complete the hourglassSum function below.
def hourglassSum(arr):
    for i in range(len(arr)-1, 0 , -1):
        print i
        print arr[i]
        for j in range(i):
            #print arr[i][j]
            pass

hourglassSum(arr)