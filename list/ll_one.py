'''
Created on Aug 28, 2017

@author: EUGENEP

abstraction
    * for humans, a car is abstracted by its subsystem such as engine, steering, gearing. 
    * ie its subsystem is unknown/abstracted
encapsulation
inheritance
polymorphism

* write code to remove dupliecates from an unsorted LL
*Return Kth to last
*delete middle node
*reverse LL

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

Node1 -> Node2 -> Node3 -> Node4
'''

class LL:
    def __init__(self, root):
        self.root = root

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class DoubleNode(Node):
    def __init__(self, data, next=None, prev=None):
        #Node.__init__(self, data, next)
        super(DoubleNode, self).__init__(data, next)
        self.prev = prev

def traverse(cur_node):
    if cur_node is not None:
        print cur_node.data
        traverse(cur_node.next)
    else:
        print "====END===="
    
def delete_node_single(LL_ref, delete_node):
    '''
    to delete:
    prev.next = cur.next
    LL may need root
    '''
    prev = None
    cur = LL_ref.root
    while True:

        if cur.data == delete_node.data:
            if prev is not None: # not starting point
                if cur.next:
                    prev.next = cur.next
                else:
                    prev.next = None
            else: # starting point to be deleted
                if cur.next:
                    LL_ref.root = cur.next
                else:
                    LL_ref.root = None
            break
        else: # not the node to delete
            if cur.next:
                prev = cur
                cur = cur.next
            else:
                break

    return

def reverse_LL(myLL):
    
    prev = None
    cur = myLL.root
    while cur is not None:
        tmp = cur.next

        cur.next = prev

        prev = cur
        cur = tmp

        if cur is None:
            myLL.root = prev
        

def delete_node_double(node):
    return

def is_cyc(head):
    return

n_one = Node(1)
n_two = Node(2)
n_three = Node(3)
n_four = Node(4)

my_LL = LL(n_one)
n_one.next = n_two
n_two.next = n_three
n_three.next = n_four


traverse(my_LL.root)
reverse_LL(my_LL)
traverse(my_LL.root)


#node_to_delete = n_three
#delete_node_single(my_LL, node_to_delete)
#traverse(my_LL.root)





