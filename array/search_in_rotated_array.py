'''
Created on Oct 4, 2017

@author: eugene

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand

i.e. 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2

you are given a target value to search. if found in the array, return its index, o/w return -1
'''
import unittest


def search(arr, tgt):
    return

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
        arr = []
        tgt = 7
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()