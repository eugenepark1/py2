'''
Created on Oct 1, 2017

@author: eugene

given an arry of ints, return indices of the two numbers such that they add up to a specific target

given [2,7,11,15] target=9

nums[0]+nums[1] = 2 + 7 = 9
return [0,1]
'''
import unittest

def return_two_sum(arr, tgt):
    tmp_dict = dict( zip(arr, [i for i,n in enumerate(arr)]) )
    
    for i,n in enumerate(arr):
        check_val = tgt - n
        if check_val in tmp_dict:
            return [i, tmp_dict[check_val]]
    
    return []

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testName(self):
        pass
    
    def test_two_sum(self):
        arr = [2,7,11,15]
        result = return_two_sum(arr, 9)
        self.assertListEqual([0,1], result, "tgt 9 => indices 0 and 1")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()