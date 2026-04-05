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