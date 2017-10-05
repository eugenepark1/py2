'''
Created on Oct 5, 2017

@author: eugenep
'''
import unittest


class Test(unittest.TestCase):


    def testName(self):
        arr = [1,2,3,4,5,6,7,7,8,9]
        n = len(arr)
        slow = arr[n-1]
        fast = arr[ arr[n-1] -1]
        
        while (slow != fast):
            slow = arr[slow-1]
            fast = arr[ arr[fast-1] -1]
            
            print "slow: %s fast: %s" % (slow,fast)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()