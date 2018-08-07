'''
Created on Aug 7, 2018

@author: eugen


find max sum of non-adjacent non-negative integers

arr: 1 2 3 4
ans 2+4

arr: 3 1 1 3 1
ans 3+3


i  value   algo                               maxList
0   3      val                                   3
1   1      max(1, maxList[0))                    3
2   1      index-2 + val                         4
3   3      index-2 + val                         6
4   1      max(index-2 + val, maxList[i-1])      6

'''


def max_sum(myList):
    maxList = []
    for index, value in enumerate(myList):
        if index == 0:
            maxList.append(value)
        elif index == 1:
            maxList.append( max(value, maxList[0]) )
        else:
            maxList.append( max(maxList[index-2]+value, maxList[index-1]) )
    
    return maxList[-1]

print max_sum([3,1,1,3,1])
            
