'''
Created on Sep 23, 2017

@author: eugene

@input: "123"
@output: 123

ord('A') 65
ord('0') 48
ord('9') 57
'''

def str_to_int(num):
    
    def is_digit(ch):
        '''
        return None if not a digit else returns int value
        '''
        ascii_value = ord(ch)
        if ascii_value < 58 and ascii_value > 47:
            return ascii_value - ord('0')
        return None
        
    sign = None
    if num[0] == '-':
        sign = -1
    elif num[0] == '+':
        sign = 1
    
    if sign is not None:
        num = num[1:]
        
    int_to_return = 0
    num_len = len(num) - 1
    for i, ch in enumerate(num):
        digit = is_digit(ch)
        if digit is None:
            raise Exception("Not an integer") 
        else:
            digit_place = num_len - i
            int_to_return += digit * (10 ** digit_place)
            
    if sign is not None:
        int_to_return = int_to_return * sign
        
    return int_to_return

print str_to_int("123")
print str_to_int("-123")
print str_to_int("+123")
print str_to_int("+ccc")
        