'''
Created on Oct 2, 2017

@author: eugenep

Like mergesort, quicksort is a divide and conquer algo
it picks an element as pivot and partitions the given array around the picked pivot
'''
def partition(arr, low, high):
    ''' This function takes last element as pivot, places the pivot element
    at its correct position in sorted array, and places all smaller to left of pivot
    and greater to right of pivot
    '''
    i = low-1
    pivot = arr[high]
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
            
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1
    

# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index
def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
        
        
arr = [10, 7, 8, 9, 1, 5]
print arr
n = len(arr)
quickSort(arr, 0, n-1)
print arr