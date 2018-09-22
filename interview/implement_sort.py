'''
Created on Sep 21, 2018

@author: eugene

insertion sort O(n^2)
selection sorts
Merge sorts
Bubble sorts
'''

def insertion_sort(arr):
    ''' 
    while not all sorted
        pick an element from unsorted (right-side)
        place the element in sorted sublist (left-side)
        
        
        |-sorted-|-unsorted-|
        i: first element in unsorted
        j: tmp ptr to move arr[i] to in sorted sublist
        
        0  1  2
        2  5  1
    '''
    def swap(arr, i, j):
        '''insert arr[i] into jth spot
        '''
        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp

    i = 0
    while i < len(arr):
        j = i
        while  (j > 0 and arr[j] < arr[j-1]):
            # find the spot in left-side
            swap(arr, j, j-1)
            print "%s %s %s" % (arr,j,j-1)
            j -= 1
        i += 1
    
    return arr

print insertion_sort([2,5,1,7,12,4,9,15,22])
