'''
Created on Sep 21, 2018

@author: eugene
'''

def insertion_sort(arr):
    ''' i: to track cur_num to move left to
        j: to track number being compared by arr[i]
    '''
    for i in range(len(arr)):
        j = i-1
        #print "%s %s %s %s" % (i, j, arr[j], arr[i])
        while  (j>0 and arr[j-1] < arr[j]):
            tmp = arr[j]
            arr[j] = arr[j-1]
            arr[j-1] = tmp
            j -= 1
            
            print "%s %s %s" % (arr,i,j)
    
    return arr

print insertion_sort([2,5,1])
