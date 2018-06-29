'''
Created on Jun 28, 2018

@author: eugenep

[]
()
{}

returns true of a string has balanced ([{}])   
'''

stacks = {
        '[' : [],
        '(' : [],
        '{' : []
    }

closedMap = {
        ']' : '[',
        ')' : '(',
        '}' : '{',
    }

opens = [i for i in stacks.iterkeys()]
def is_balanced(input_str):
    for ch in input_str:
        if ch in opens:
            stacks[ch].append(ch)
        else: # closed
            open_counterpart = closedMap[ch]
            if len(stacks[open_counterpart]) == 0:
                return False # you have a close bracket before an open one
            else:
                popped = stacks[open_counterpart].pop()
                #if popped != open_counterpart:
                #    return False 
    return True
            
assert is_balanced("()") is True
assert is_balanced("())") is False
assert is_balanced("((()))") is True
assert is_balanced(")(") is False
assert is_balanced("(){}[](())") is True
print "all passed"