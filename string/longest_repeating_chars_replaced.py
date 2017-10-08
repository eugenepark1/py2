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
        
        s_one = "AAABCD"
        s_one = "AAABAAABAAAB"
        
        cur_str = [i for i in s_one] + [None]
        
        
        i = 0
        prev_char = None
        prev_char_len = 0

        X = {}
        Y = {}
        add_prev = False
        add_prev_i = 0
        while True:
            print "%s\n\t%s, %s" % (cur_str[i], prev_char, prev_char_len)
    
            if cur_str[i] is None:
                break
            
            
            if prev_char is None: 
                prev_char = cur_str[i]
                prev_char_len = 1
            elif cur_str[i] == prev_char:
                prev_char_len += 1
            elif cur_str[i-1] == cur_str[i+1]: # diff char (mid) 
                
                if add_prev:
                    X[add_prev_i] += prev_char_len
                    X[i] = prev_char_len
                    add_prev_i = i
                else:
                    X[i] = prev_char_len
                    add_prev = True
                    add_prev_i = i

                prev_char_len = 0
            else: # diff char (end)
                if add_prev:
                    X[add_prev_i] += prev_char_len
                    add_prev = False
                
                X[i] = prev_char_len
                prev_char_len = 0
                    
                
                
                

                
                # Z means depends on the prev char changed
                # X means change it
                # 0  1  2 X|3 Z/1  Z/2
                # A  A  A  B   C    D
                
                # 0  1  2 X|6,add 0  1  2  X|6,add           X|3
                # A  A  A    B    A  A  A     B     A  A  A  B   None

            i += 1
                
        print X
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()