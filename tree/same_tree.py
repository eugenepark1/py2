'''
Created on Oct 4, 2017

@author: eugene

given two binary trees, write a function to check if they are equal or not
Two binary trees are considered equal if they are structurally identical and the nodes have the same value
'''



class Node():
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def is_same(node1, node2):
    if node1 is None and node2 is None:
        return True

    elif node1.data == node2.data:
        return is_same(node1.left, node2.left) and is_same(node2.right, node2.right)
    
    return False


one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)

one.left = two
one.right = three
two.left = four
three.right = five

print is_same(one, three)