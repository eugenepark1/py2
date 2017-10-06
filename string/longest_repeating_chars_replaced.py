'''
Created on Oct 6, 2017

@author: eugenep

given a string that consists of only uppercase English letters,
you can replace any letter in the string with another letter at most k times

Find the length of a longest substring containing all repeating letters you can get after performing the above ops

s="ABAB" k=2
output 4
replace "B' and "B", AAAA

s="AABABBA" k=1
output 4
replace 'B', AAAABBA

s="AAAA" k=1
output 4
no replace
'''
import unittest


class Test(unittest.TestCase):


    def testName(self):
        '''
        1. what to do
            replace chars k times (at most)
        2. when to what to do
            * if str[i-1] == str[i+1] and str[i] != str[i-1], then candidate for str[i] = str[i-1] 
            or
            * if str[i-1] != str[i]
            * if str[i+1] != str[i]
            
            ID nonrepeated char while tracking the length of repeated chars
            
            * for above ops -> length of substr of repeated chars
        
        '''
        
        s_one = "ABAB"
        s_two = "AABABBA"
        s_three = "AAAA"
        
        cur_str = s_one
        
        
        def extend_arr(arr, i):
            return
        candidates = []
        
        prev_chr = None
        prev_repeated = 0
        for ind, chr in enumerate(cur_str):
            if prev_chr is None:
                chr = prev_chr
            elif chr == prev_chr:
                # no need to convert this
                prev_repeated += 1
            else:
                # possible convert this
                if chr != cur_str[ind+1]:
                    candidates.append( (ind, prev_repeated+1) ) # this isnt looking forward
                else:
                    # still candidate but need correct prev_repated o/w length of substr for repeated chrs
        
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()