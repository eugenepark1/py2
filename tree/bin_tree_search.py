'''
Created on Aug 29, 2017

@author: EUGENEP

BST
1) left child is less than parent
2) right child is greater than parent
3) this must be true for all descendents

access: O(log n)
search: O(log n)
insert: O(log n)
delete: O(log n)

two common types of balanced trees are red-black trees and AVL trees


complete binary tree:  tree in which every level of the tree is fully filled except for the last level
full binary tree: every node is either zero or two children - no nodes have only one child
perfect binary tree: both full and complete


'''
#inorder: 
def in_rec(node):
    if node is not None:
        in_rec(node.left)
        print node.data
        in_rec(node.right)
#preorder
def pre_rec(node):
    if node is not None:
        print node.data
        pre_rec(node.left)
        pre_rec(node.right)
    
#postorder
def post_rec(node):
    if node is not None:
        post_rec(node.left)
        post_rec(node.right)
        print node.data


# A binary tree node
class Node:
     
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def setRoot(self, val):
        self.root = Node(val)

    def insert(self, val):
        if(self.root is None):
            self.setRoot(val)
        else:
            self.insertNode(self.root, val)

    def insertNode(self, currentNode, val):
        if(val <= currentNode.data):
            if(currentNode.left):
                self.insertNode(currentNode.left, val)
            else:
                currentNode.leftChild = Node(val)
        elif(val > currentNode.data):
            if(currentNode.right):
                self.insertNode(currentNode.right, val)
            else:
                currentNode.right = Node(val)

    def find(self, val):
        return self.findNode(self.root, val)

    def findNode(self, currentNode, val):
        if currentNode is None:
            return False
        elif val == currentNode.val:
            return True
        elif val < currentNode.val:
            return self.findNode(currentNode.leftChild, val)
        else:
            return self.findNode(currentNode.rightChild, val)
        
        

one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)

myBST = BST()
myBST.insert(1)
myBST.insert(2)
myBST.insert(3)
myBST.insert(4)
myBST.insert(5)

in_rec(myBST.root)
print "======="
pre_rec(myBST.root)
print "======="
post_rec(myBST.root)
print "======="

