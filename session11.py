#LINKED LIST LECTURE 2

#multiple pass technique
'''
- traverse a LL multiple times to get info or process nodes
- common applications:
    - length of LL
    - performing operations that need global info about the LL
'''
#temporary head technique
'''
- create a temp head node to handle edge cases involving acc head
- typically what we need to return
- common applications:
    - deleting head without losing rest of LL
    - updating head
'''
#slow-fast pointer technique
'''
- two pointers moving at diff speeds to solve problems with cycle detection or general LL
- common applications:
    - detecting cycle in LL (lapping people on a track)
    - finding middle node
    - finding length of cycle
'''
#doubly linked list -- curr.next AND curr.prev (connection goes both ways)
# ------------------------- instructor demo -------------------------
'''
write a function to find the middle node of a singly linked list.
if the list has an even number of nodes, return the second middle node.
'''
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def findMiddleNode(head):
    #U  #we know we cant go backwards, we know maybe keep track of the head, maybe need a counter to keep track of how long, or maybe i need 2+ pointers
        #input: head node
        #output - middle node (not the value)
    #M  #navigate thru LL, middle (find point, need to know how long the LL is/go to the end). how do i get back ?
        #head node
        #two pointer -> middle -> 1/2, slow=1 fast=2
    #P  #1. working head node, lets keep track in teh beginning (can delete if we dont need)
        #2. make 2 pointers (slow and fast), start all nodes at head
        #3. fast is 2x faster than slow to give the middle
        #4. we only know the middle when fast reaches the end (None)
        #5. return Node object (not just the value)
    
    if(head==None): #edge case
        return None

    #tempHead = head
    slow = head
    fast = head
    #tempHead = slow = fast = head

    #how do we know we have reached the end
    while(fast is not None and fast.next is not None):
        fast = fast.next.next
        slow = slow.next

    return slow
 

a = Node(1)
b = Node(2)
c = Node(3) 
d = Node(4) #*
e = Node(5)
f = Node(6)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

middleNode = findMiddleNode(a)
print(middleNode.val)