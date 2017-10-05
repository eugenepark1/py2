'''
Created on Oct 4, 2017

@author: eugene

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand

i.e. 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2

you are given a target value to search. if found in the array, return its index, o/w return -1
'''
import unittest


def findMin(arr):
    # [4,5,6,7,0,1,2]
    low = 0
    high = len(arr) - 1
    while (low < high):
        mid = (low + high) / 2
        
        # found the middle minimum
        if (mid > 0 and arr[mid] < arr[mid -1]):
            return arr[mid]
        
        # move either low->mid or mid<-high
        if (arr[low] <= arr[mid] and arr[mid] > arr[high]):
            low = mid + 1
        else:
            high = mid - 1
        
    return arr[low]

def search(arr, tgt):
    low = 0
    high = len(arr) - 1
    
    while low < high:
        mid = (low + high) / 2
        
        if (arr[mid] < arr[0] and tgt < arr[0]):
            num = arr[mid]
        else:
            if tgt < arr[0]:
                num = -float("inf")
            else:
                num = float("inf")

        if (num < tgt):
            low = mid + 1
        elif (num > tgt):
            high = mid
        else:
            return mid
    
    return -1

def binsearch(arr, tgt):
    
    if len(arr) == 1:
        if arr[0] == tgt:
            return True
        else:
            return False

    mid = len(arr)/2
    if tgt == arr[mid]:
        return True
    
    if tgt < mid:
        return binsearch(arr[:mid], tgt)
    else:
        return binsearch(arr[mid:], tgt)


class Test(unittest.TestCase):


    def testName(self):
        pass
    
    def test_binsearch(self):
        arr = [0,1,2,4,5,6,7]
        arr_pivoted = [4,5,6,7,0,1,2]
        tgt = 0
        exists = binsearch(arr, tgt)
        index = search(arr_pivoted, tgt)
        min = findMin(arr_pivoted)

        self.assertEqual(exists, True, "binsearch")
        self.assertEqual(index, 4, "pivoted")
        self.assertEqual(min, 0, "min")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()