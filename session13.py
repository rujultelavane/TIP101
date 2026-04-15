#INTRO TO BINARY TREES LECTURE
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class ListNode:
    def __init__(self, key):
        self.val = key
        self.next = None

# Creating a root node
root = TreeNode(13)

# Creating children nodes
root.left = TreeNode(6)
root.right = TreeNode(21)

# NODE INSERTION
'''
        13
      /    \
     6      21
    /\      / \
   4  8    15  21
                \
                24
                / \
             (22)  26

'''
'''
- start at root
- compare value to be inserted with current root value
- if value less, move to left, if greater, move to right
- repeat above until correct spot found
'''

# NODE DELETION
'''
cases:
 1. no children (leaf)
    - assign node to null
 2. one child
    - swap node and child
    - remove target node (now a leaf)
 3. two children (successor: next highest num, predecessor: next lower num)
    - swap node to be deleted with successor 
    - delete node
'''