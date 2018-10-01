'''
Created on Sep 21, 2018

@author: eugene

quicksort  O(nlogn) aka partition-exchange sort 
Merge sort O(nlogn)
insertion sort O(n^2)
selection sort
Bubble sort

'''
def swap(arr, x, y):
    tmp = arr[x]
    arr[x] = arr[y]
    arr[y] = tmp
    
def quicksort_old(arr, lo, hi):
    '''
    algorithm quicksort(A, lo, hi) is
    if lo < hi then
        p := partition(A, lo, hi)
        quicksort(A, lo, p - 1 )
        quicksort(A, p + 1, hi)

    algorithm partition(A, lo, hi) is
        pivot := A[hi]
        i := lo    
        for j := lo to hi - 1 do
            if A[j] < pivot then
                swap A[i] with A[j]
                i := i + 1
        swap A[i] with A[hi]
        return i
        ss
    '''
    '''
    def partition(arr, lo, hi):

        pivot = arr[hi]
        i = lo
        for j in range(lo, hi-1):
            if arr[j] < pivot:
                swap(arr, i, j)
                i += 1
        
        swap(arr, i, hi)
        return i
    '''
    
    def partition_old(arr, lo, hi):

        pivot = arr[hi]
        i = lo # keep track of which items are less than pivot
        for j in range(lo, hi-1):
            if arr[j] < pivot:
                swap(arr, i, j)
                i += 1
        
        swap(arr, i, hi)
        
        return i
    print
    print "quicksorting %s" % arr
    if lo < hi:
        p = partition(arr, lo, hi)
        print "\tafter partitioned: %s %s" % (arr, arr[p])
        print "\tquicksorting: %s" % (arr[lo:p-1])
        print "\tquicksorting: %s" % (arr[p+1:hi])
        quicksort(arr, lo, p-1)
        quicksort(arr, p+1, hi)

    return arr


# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot
def partition(arr, low, high):
    i = ( low-1 )         # index of smaller element
    pivot = arr[high]     # pivot
    for j in range(low , high):
        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
 
    arr[i+1],arr[high] = arr[high],arr[i+1]

    return ( i+1 )
 
# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index
 
# Function to do Quick sort
def quicksort(arr, low, high):
    #print
    #print "quicksorting %s" % arr
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)
        # Separately sort elements before
        # partition and after partition
        quicksort(arr, low, pi-1)
        quicksort(arr, pi+1, high)
        
    return arr


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
print quicksort([2,5,1,7,12,4,9,15,22], 0, len([2,5,1,7,12,4,9,15,22])-1)
