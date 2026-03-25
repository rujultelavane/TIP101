# ------------------------- linked list lecture 1 -------------------------

#OOP
'''
class - fundamentl to oop
- help in modeling real-world entities, making code reusable, organizing complex programs
instantiating -- making an instance of a class
making a class:
'''

'''
class MyClass:
    def __init__(self, param1, param2): #initializes -- NECESSARY
        self.param1 = param1
        self.param2 = param2
    def my_method(self):
        return self.param1+self.param2
'''

#LINKED LISTS
'''
- arrays dont dynamically grow, linkedlists can
'''

#create node class 
class Node:
    def __init__(self, value, value2=None): #value2 is optional
        self.value = value
        self.next = None

a = Node(2)
b = Node(3)
c = Node(4)
d = Node(7)
e = Node(6)
a.next = b
b.next = c
c.next = d
d.next = e

#iterate thru linked list
curr = a #pointer
while(curr != None):
    if(curr.value == 7):
        print("lucky!")
    curr = curr.next

b = None
print(a.value)
print(b.value)
