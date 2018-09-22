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
    def insert(arr, i, j):
        '''insert arr[i] into jth spot
        '''
        tmp = arr[i]
        # shift items from jth by one to right for until i-1th item
        k = i
        while k >=j:
            arr[k] = arr[k-1]
            k -=1
            
        arr[j] = tmp

    i = 0
    while i < len(arr):
        j = i-1
        do_swap = False
        while  (j > 0 and arr[i] < arr[j]):
            # find the spot in left-side
            j -= 1
            do_swap = True
            #print "%s %s %s" % (arr,i,j)
        
        if do_swap:
            print "insert(%s, %s, %s)" % (arr,i,j)
            insert(arr, i , j)
        i += 1
    
    return arr

print insertion_sort([2,5,1,7,12,4,9,15,22])
