'''
Created on Sep 21, 2017

@author: eugenep
'''
# 2 -> 5 -> 6 -> 10 -> 3 -> 7 -> 12
# give nth from the end, only with linked list


from ll_one import Node, LL

two = Node(2)
five = Node(5)
six = Node(6)
ten = Node(10)
three = Node(3)
seven = Node(7)
twelve = Node(12)

my_LL = LL(two)

two.next = five
five.next = six
six.next = ten
ten.next = three
three.next = seven
seven.next = twelve

def get_nth_from_end(nth, start):
    cur = start
    cnt = 0
    nth_ptr = None
    while cur.next:
        cnt += 1
        
        if nth_ptr is None and cnt == nth:
            nth_ptr = start
        elif nth_ptr:
            nth_ptr = nth_ptr.next
            
        cur = cur.next

    return nth_ptr.data

print get_nth_from_end(3, my_LL.root)

