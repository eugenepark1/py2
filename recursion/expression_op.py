'''
Created on Aug 26, 2017

@author: eugene
'''
'''
    +
 +     +
1 2   3 4 
'''

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        
        
PLUS = '+'
plus_one = Node(PLUS)
plus_two = Node(PLUS)
plus_three = Node(PLUS)
left_left = Node(1)
left_right = Node(2)
right_left = Node(3)
right_right = Node(4)

plus_one.left = plus_two
plus_one.right = plus_three

plus_two.left = left_left
plus_two.right = left_right

plus_three.left = right_left
plus_three.right = right_right


def evaluate_op(node):
    if node.left and node.right:
        if node.data == PLUS:
            return evaluate_op(node.left) + evaluate_op(node.right)
    else:
        return node.data


print evaluate_op(plus_one)