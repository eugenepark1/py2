'''
Created on Sep 22, 2017

@author: eugene

given a stream of integers (1,9) find median at any given time

You need a min-heap and a max-heap.

Min-heap will contain the maximum half of the numbers from the array. 
Max-heap will contain the minimum half of the numbers from the array.

So the top value from the min-heap will be the minimum number from the max half of the array. 
The top value from the max-heap will be the maximum number from the min half of the array.


So you pretty much have the middle values of the array, therefore can calculate the median. So think about it, what can you change to make it work with odd number of values?



1 3 4 5 7
max-heap    min-heap
4             4
3             5
1             7


1, 3, 4
max-heap    min-heap
3              1
1              3
               4



iterate:

'''


