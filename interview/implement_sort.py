'''
Created on Sep 21, 2018

@author: eugene

Merge sort O(nlogn)
insertion sort O(n^2)
selection sort
Bubble sort
'''


def merge_sort(arr):
    if len(arr) == 1:
        return arr
    
    mid = len(arr)/2
    left_sorted = merge_sort(arr[:mid])
    right_sorted = merge_sort(arr[mid:])

    
    combined_sorted = []
    i,j = 0,0
    while (i < len(left_sorted) and j < len(right_sorted)):
        if left_sorted[i] < right_sorted[j]:
            combined_sorted.append(left_sorted[i])
            i += 1
            
            if i == len(left_sorted):
                combined_sorted += right_sorted[j:]
                j = len(right_sorted)
            
        else:
            combined_sorted.append(right_sorted[j])
            j += 1
            
            if j == len(right_sorted):
                combined_sorted += left_sorted[i:]
                i = len(left_sorted)
    
    #print "check===="
    #print combined_sorted
    #print sorted(left_sorted + right_sorted)
    #print "end check==="
    return combined_sorted

def insertion_sort(arr):
    ''' 
    while not all sorted
        pick an element from unsorted (right-side)
        place the element in sorted sublist (left-side)
        
        
        |-sorted-|-unsorted-|
        i: first element in unsorted
        j: tmp ptr to move arr[j]
        
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
            #print "%s %s %s" % (arr,j,j-1)
            j -= 1
        i += 1
    
    return arr

print insertion_sort([2,5,1,7,12,4,9,15,22])
print merge_sort([2,5,1,7,12,4,9,15,22])
