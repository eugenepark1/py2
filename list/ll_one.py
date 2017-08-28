'''
Created on Aug 28, 2017

@author: EUGENEP

abstraction
    * for humans, a car is abstracted by its subsystem such as engine, steering, gearing. 
    * ie its subsystem is unknown/abstracted
encapsulation
inheritance
polymorphism

Q1) write code to remove dupliecates from an unsorted LL
Return Kth to last
delete middle node
partition 
3->5->8->5->10->2->1 [partition 5)
3->1->2->10->5->5->8

palindrome
loop detection
sumlist


class Base(object):
    def __init__(self):
        print "Base created"

class ChildA(Base):
    def __init__(self):
        Base.__init__(self)

class ChildB(Base):
    def __init__(self):
        super(ChildB, self).__init__()

ChildA() 
ChildB()
'''

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class DoubleNode:
    def __init__(self, data, next=None, prev=None):
        Node.__init__(self, data, next)
        self.prev = prev

def delete_node_single():
    return

def delete_node_double():
    return

def is_cyc(head):
    return

