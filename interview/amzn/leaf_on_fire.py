'''
Created on Sep 18, 2018

@author: eugenep
'''

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        
'''
              4
       5              8
    7    10       12    3
                9
'''

oneNode = Node(4)
twoNode_left = Node(5)
twoNode_right = Node(8)
oneNode.left = twoNode_left
oneNode.right = twoNode_right

threeNode_left_left = Node(7)
threeNode_left_right = Node(10)
twoNode_left.left = threeNode_left_left
twoNode_left.right = threeNode_left_right

threeNode_right_left = Node(12)
threeNode_right_right = Node(3)
twoNode_right.left = threeNode_right_left
twoNode_right.right = threeNode_right_right

fourNode_right_left_left = Node(9)
threeNode_right_left.left = fourNode_right_left_left


def get_path(root, node):
    
    
    if root is None:
        print "root is None"
        return {'path': [],
                'found': False
            }
    
    elif root.value == node.value:
        print "root is equal to value (%s %s)" % (root.value, node.value)
        
        print "found %s" % root.value
        return {'path': [node.value],
                'found': True
                }
    else:
        print "else: %s" % root.value
        
        left = get_path(root.left, node)
        right = get_path(root.right, node)
        
        print "left: %s (%s)" % (left, root.value)
        print "right: %s (%s)" % (right, root.value)
    
        
        if left['found']:
            return {'path': [root.value] + left['path'],
                    'found': True
                }
        elif right['found']:
            return {'path': [root.value] + right['path'],
                    'found': True
                }
        else:
            return {'path': [],
                'found': False
            }
 
 
print get_path(oneNode, fourNode_right_left_left)
    
def gather_nodes(root):
    if root is None:
        return []
    else:
        return [root.value] + gather_nodes(root.left) + gather_nodes(root.right)

def calculate_time_to_burn(root, fireLeaf):
    t = 0
    
    notVisitedNodes = gather_nodes(root)
    latest_fire_nodes = [fireLeaf]
    while len(notVisitedNodes) > 0:
        
        # step
        for f_node in latest_fire_nodes:
            notVisitedNodes.remove(f_node.value)

            # add parent, childrent to latest_fire_nodes
            f_node_path = get_path(root, f_node)
            
            
        t += 1
    
    return t
    

#calculate_time_to_burn(oneNode, threeNode_right_right)
    