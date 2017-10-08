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
from curses.ascii import CAN


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
        
        i = 0
        candidates = {}
        prev_char = None
        prev_char_len = 0
        
        delayed_reset = False
        
        # goal
        # candidates = {
        #    1 : 7
        #    2 : 7
        #    3 : 4
        #}
        def look_ahead():
            return
        
        keep_going = False
        keep_going_index = 0
        while i < len(cur_str):
            if prev_char is None:
                prev_char == cur_str[i]
                prev_char_len = 1
            elif cur_str[i] == prev_char:
                prev_char_len += 1
            else: # different chr found
                if cur_str[i-1] == cur_str[i+1]:
                else:
                    candidates[i] = prev_char_len
                
                
                if keep_going: # (2)
                    # need to record (1)
                    candidates[keep_going_index] = prev_char_len
                    
                else: # not keep_going
                    if cur_str[i-1] == cur_str[i+1]: # (1)
                        keep_going = True
                        prev_char_len += 1
                        keep_going_index = i
                        
                    else: #(3)
                        
                # reset or not
                #       1      2/1      3
                # A A A B A A A B A A A B C
                
                # Z means depends on the prev char changed
                # X means change it
                # 0  1  2 X|3 Z/1  Z/2
                # A  A  A  B   C    D
                
                # 0  1  2 X|6 0  1  2  X|3
                # A  A  A  B  A  A  A  B

                    
                
                
            i += 1
                

        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()