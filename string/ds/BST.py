'''
Created on Jun 29, 2018

@author: eugenep
'''
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