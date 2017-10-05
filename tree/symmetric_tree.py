'''
Created on Oct 4, 2017

@author: eugene
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


ofive = Node(5)
osix = Node(6)
onine = Node(9)
oseven = Node(7)
oeight = Node(8)
oten = Node(10)

mfive = Node(5)
msix = Node(6)
mnine = Node(9)
mseven = Node(7)
meight = Node(8)
mten = Node(10)


print is_same(ofive, mfive)