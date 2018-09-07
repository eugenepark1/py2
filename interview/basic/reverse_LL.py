'''
Created on Sep 6, 2018

@author: eugenep
'''

class LL:
    def __init__(self, root):
        self.root = root

    def traverse(self):
        traverse_str = ""
        cur = self.root
        while cur is not None:
            if cur.next is None:
                traverse_str += "%s" % cur
            else:
                traverse_str += "%s->" % cur
            cur = cur.next
        print traverse_str
    
    def reverse(self):
        cur = self.root
        prev = None
        while cur is not None:
            tmp = cur.next
            cur.next = prev
            
            # prep for next iteration
            prev = cur
            cur = tmp
        self.root = prev
        
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
    def __str__(self):
        return str(self.data)
        

n_one = Node(1)
n_two = Node(2)
n_three = Node(3)
n_four = Node(4)

my_LL = LL(n_one)
n_one.next = n_two
n_two.next = n_three
n_three.next = n_four

my_LL.traverse()
my_LL.reverse()
my_LL.traverse()