'''
Created on Jun 29, 2018

@author: eugene
'''


# b - index of the beginning
# e - index of the element to the right of the last one
# [  arr  ]
# b        e
# [1, 2, 3, 4]
# [0, 2) [2, 4)
# l - length, b e, s = (b+e)/2
# [b, s) [s, e)

#  0  1  2  3
# [b, e)
# mergeSort(arr, 0, 2) -> [1, 2]

# [1, 1)


def mergeSort(arr):
    return mergeSortAux(arr, 0, len(arr))

def mergeSortAux(arr, b, e):
    if b == e:
        return []
    if b + 1 == e:
        return arr[b:e]
    s = (b+e) // 2 
    L = mergeSortAux(arr, b, s)   # sorted left half of arr
    R = mergeSortAux(arr, s, e)   # sorted right half of arr
    arr = merge(L, R)             # merge L and R
    return arr
    
# PRECONDITION: L and R are sorted
    # put stuff in res
    #    i      
    # L []
    # R [2 3 4]
    #    j
def merge(L, R):
    res = []
    i = 0
    j = 0
    while (i < len(L)) or (j < len(R)):
        if j >= len(R) or (i < len(L) and L[i] < R[j]):
            res.append(L[i])
            i += 1
        else:
            res.append(R[j])
            j += 1
    return res
    
    
#arr = [13, 12, 4, 1, 2, 34, 123, 51, 1, 2]
#print(mergeSort(arr))

############################################################################

#        2
#     5     3   
#    6 7   4     

#  0  1  2  3  4  5 
# [2, 5, 3, 6, 7, 4]

#1 

# HEAP SORT

def parent(i):
    return (i-1) // 2

def leftChild(i):
    return 2*i + 1

def rightChild(i):
    return 2*i + 2

#    p
#  l   r

# PRECONDITION: arr stores a heap, but the first element can be wrong
def heapify(arr, p):
    if p >= len(arr):
        return
    l = leftChild(p)
    r = rightChild(p)
    smallest = p
    if l < len(arr) and arr[l] < arr[smallest]:
        smallest = l
    if r < len(arr) and arr[r] < arr[smallest]:
        smallest = r
    swap(arr, p, smallest)
    if smallest != p:
        heapify(arr, smallest)
    return 

def swap(arr, i, j):
    # pro trick
    arr[i], arr[j] = arr[j], arr[i]
    #temp = arr[i]
    #arr[i] = arr[j]
    #arr[j] = temp

# turns arr into a heap
def makeHeap(arr):
    for i in reversed(range(len(arr) // 2)):
        heapify(arr, i)

def heapSort(arr):
    res = []
    # we have to make arr into a heap
    makeHeap(arr)
    while arr: # <- while there is something in the arr
        res.append(arr[0])
        arr[0] = arr[-1] # put the last elem in index 0
        arr.pop()
        heapify(arr, 0)
    return res

#        2
#     5     3   
#    6 7   4     

# [2, 5, 3, 6, 7, 4]
#arr = [13, 12, 4, 1, 2, 34, 123, 51, 1, 2]
#print(heapSort(arr))


# arr = [0, 1, 2, 3, 4, 5]
# b = 1, e = 5
# looking at [1, 2, 3, 4]

#here the arr actually changes len

def kMergeSort(arr, k):
    k = min(k, len(arr))
    #print(arr)
    if len(arr) <= 1:
        return arr
    # divide into k segments each with m elems (except maybe the last one)
    m = len(arr) // k   # length of the segment
    segments = []
    for i in range(k):
        # look at segment nr i
        # what would be segment nr 0 ? -> arr[b, b + m]
        # what would be segment nr 1 ? -> arr[b + m, b + 2m] 
        segB = i*m
        segE = (i+1)*m if i < k - 1 else len(arr)
        seg = arr[segB:segE]
        # sort that segment and put it in segments
        segments.append(kMergeSort(seg, k))
    #arr = kMerge(segments, k)
    arr = kNormalMerge(segments)
    return arr
    
def kMerge(segments, k):
    print(segments)
    res = []
    # [2, 4, 6]
    # [1, 2, 3]
    # [4, 5, 7]
    heap = []
    for i in range(k):
        if not segments[i]:
            continue
        heap.append( (segments[i][0], i) )
        segments[i].pop(0)
    makeHeap(heap)
    while heap:
        minVal = heap[0][0]
        minInd = heap[0][1]
        res.append(minVal)
        if segments[minInd]:
            # if there is a next elemnt in that segment
            # we can put it in the heap
            heap[0] = (segments[minInd][0], minInd)
            segments[minInd].pop(0)
            heapify(heap, 0)
        else:
            # there is no next elem in that segment
            heap[0] = heap[-1]
            heap.pop()
            heapify(heap, 0)
    return res

def kNormalMerge(segments):
    print(segments)
    res = segments.pop(0)
    for each in segments:
        i = 0
        while len(each) > 0:
            print(segments)
            print(res)
            if (each[0] <= res[0]):
                res.insert(0, each.pop(0))
            else:
                i += 1
                if (i == len(res)) or (each[0] <= res[i]):
                    res.insert(i, each.pop(0))
    return(res)

arr = [23, 12, 2, 41, 111, 36, 123, 11, 3, 2]
#arr = [1, 3]
print(kMergeSort(arr, 4))