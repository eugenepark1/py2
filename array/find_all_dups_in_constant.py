'''
Created on Oct 5, 2017

@author: eugenep
'''
import unittest


class Test(unittest.TestCase):


    def test_find_dups(self):
        arr = [4,3,2,7,8,2,3,1]
        expected = [2,3]
        
        res = []
        ''' 
        given array of ints, 1 <= a[i] <= n, size of array
        find number i, flip the number at position i-1 to neg
        if the number at position i-1 is already neg, i is the number that occurs twice
        '''


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_find_dups']
    unittest.main()