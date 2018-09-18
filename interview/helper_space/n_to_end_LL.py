'''
Created on Sep 7, 2018

@author: eugenep

using extra ptr ie space improve from O(n^2) to O(n)

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

def n_to_the_end(n, root):
    cur = root
    nth_node = None
    tmp_cnt = 0
    while cur is not None:
        
        cur = cur.next
    
    return nth_node

