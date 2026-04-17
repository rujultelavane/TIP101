# # class TreeNode():
# #      def __init__(self, value, left=None, right=None):
# #          self.val = value
# #          self.left = left
# #          self.right = right
         
# # def is_univalued(root):
# #     num = root.val
# #     if root.left is None or root.right is None: #base case - reached end of tree
# #         return True
# #     if root.left.val == num and root.right.val == num: #check if they equal parent node and each other
# #         return is_univalued(root.left) and is_univalued(root.right)
# #     else: 
# #         return False



# # Problem 2

# def height(root):
#     # check both right and left 
#     # if both right and left continue both
#     # if only right continue right same w left
    
#     if root is None:
#         return 0
    
#     return 1 + max(height(root.left), height(root.right))



# # root = TreeNode(1) 
# # root.left = TreeNode(1) 
# # root.right = TreeNode(1) 
# # root.left.left = TreeNode(2) 
# # root.left.right = TreeNode(1) 
# # root.right.right = TreeNode(1)
# # print(height(root))

class TreeNode():
     def __init__(self, key, value, left=None, right=None):
            self.key = key
            self.val = value
            self.left = left
            self.right = right

def print_tree(root, level=0):
    if root is None:
        return

    print_tree(root.right, level + 1)
    print("    " * level + str(root.val))
    print_tree(root.left, level + 1)

def insert(root, key, value):
    # if root is none then return key
    if root is None:
        root = TreeNode(key, value)
	# if key < root -> put in left subtree
    if key < root.key:
        if not root.left:
            root.left = TreeNode(key, value)
        else:
            insert(root.left, key, value)

    # if key > root -> put it right subtree
    if key > root.key:
        if not root.right:
            root.right = TreeNode(key, value)
        else:
            insert(root.right, key, value)
    
    #if key = root -> replace it
    else:
        root.value = value
    
    return root

def remove

root = None
root = insert(root, 10, "A")
print_tree(root)
print(" ======================= Test 1 =====================")

root = None
root = insert(root, 10, "A")
insert(root, 5, "B")
print_tree(root)
print(" ======================= Test 2 =====================")

root = None
root = insert(root, 10, "A")
insert(root, 15, "B")
print_tree(root)
print(" ======================= Test 3 =====================")

root = None
vals = [(10, "A"), (5, "B"), (15, "C"), (2, "D"), (7, "E"), (12, "F"), (20, "G")]

for k, v in vals:
    root = insert(root, k, v)

print_tree(root)
print(" ======================= Test 44 =====================")

root = None
root = insert(root, 10, "A")
insert(root, 10, "UPDATED")
print_tree(root)
print(" ======================= Test 5 =====================")