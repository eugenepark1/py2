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
        return {'path': [],
                'found': False
            }
    
    elif root.value == node.value:
        return {'path': [node.value],
                'found': True
                }
    else:
        left = get_path(root.left, node)
        right = get_path(root.right, node)
        
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
 
 
def gather_nodes(root):
    if root is None:
        return []
    else:
        return [root] + gather_nodes(root.left) + gather_nodes(root.right)

notVisitedNodes = []
    
def calculate_time_to_burn(root, fireLeaf):
    global notVisitedNodes
    t = 0
    notVisitedNodes = gather_nodes(root)
    
    latest_fire_nodes = [fireLeaf]
    while len(notVisitedNodes) > 0:
        
        
        tmp_latest_fire_nodes = []
        # step
        for f_node in latest_fire_nodes:
            notVisitedNodes.remove(f_node)

            # add parent, childrent to latest_fire_nodes
            f_node_path = get_path(root, f_node)
            if len(f_node_path) > 1:
                parent = f_node_path['path'] = -2
                
                # add parent to latest firenode
                for node in notVisitedNodes:
                    if node.value == parent:
                        tmp_latest_fire_nodes.append(node)
                
            # add children to latest fire nodes
            for node in notVisitedNodes:
                try:
                    if node.value == f_node.left.value:
                        tmp_latest_fire_nodes.append(f_node.left)
                except:
                    pass
            for node in notVisitedNodes:
                try:
                    if node.value == f_node.right.value:
                        tmp_latest_fire_nodes.append(f_node.right)
                except:
                    pass
        latest_fire_nodes = tmp_latest_fire_nodes
            
        t += 1
        print t
    
    return t
    
print get_path(oneNode, fourNode_right_left_left)
print [node.value for node in gather_nodes(oneNode)]
print calculate_time_to_burn(oneNode, threeNode_right_right)
    