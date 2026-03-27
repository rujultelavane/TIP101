class Pokemon():
	def  __init__(self, name, hp, damage):
		self.name = name
		self.hp = hp # hit points
		self.damage = damage # The amount of damage this pokemon does to its opponent every attack
	'''
	Then, write a method attack() that takes in a Pokemon object opponent and decreases opponent's hp by their self's damage amount.

    If damaging the opponent leads to the opponent having an hp of 0 or less, the function should set the opponent's hp to 0 and print out "<Opponent name> fainted>.

    Otherwise, the function should print out "<Pokemon name> dealt <damage> damage to <opponent name>"
	'''	
	def attack(self, opponent):
		opponent.hp -= self.damage
		if opponent.hp <= 0:
			opponent.hp = 0
			print(f"{opponent.name} fainted.")
		else:
			print(f"{self.name} dealt {self.damage} damage to {opponent.name}")
        
pikachu = Pokemon("Pikachu", 35, 20)
bulbasaur = Pokemon("Bulbasaur", 45, 30) 

opponent = bulbasaur
pikachu.attack(opponent)
#Example Output: Pikachu dealt 20 damage to Bulbasaur


#2. Convert to Linked List

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
	'''
	takes in a head of a linked list and a new_node from the Node class as parameters.
    It should insert new_node as the new head of the linked_list. The function returns new_node.
	'''

def add_first(head, new_node):
	new_node.next = head

	return new_node


node_1 = Node("Jigglypuff")
node_2 = Node("Wigglytuff")

node_1.next = node_2

print(node_1.value, "->", node_1.next.value)
print(node_2.value, "->", node_2.next)

'''
Jigglypuff -> Wigglytuff
Wigglytuff -> None
'''

#Problem #3 - Add First

# Using the Linked List from Problem 2
print(node_1.value, "->", node_1.next.value)

new_node = Node("Ditto")
node_1 = add_first(node_1, new_node)

print(node_1.value, "->", node_1.next.value)

'''
Jigglypuff -> Wigglytuff 
Ditto -> Jigglypuff
'''


# Using the Linked List from Problem 2
print(node_1.value, "->", node_1.next.value)

new_node = Node("Ditto")
node_1 = add_first(node_1, new_node)

print(node_1.value, "->", node_1.next.value)

#Problelm #4: Get Tail
'''
takes in the head of a linked list as a parameter
Return the value of the tail. If the list is empty, return None.
'''
def get_tail(head):
	if head == None:
		return None
	curr = head
	while curr.next != None:
		curr = curr.next
	return curr.value

# Build: num1 -> num2 -> num3
num1 = Node("num1")
num2 = Node("num2")
num3 = Node("num3")
num1.next = num2
num2.next = num3

head = num1
tail = get_tail(head)   # or get_tail(num1)
print(tail)             # expected: num3

#Problem 5: Replace Node
'''
updates in place every node whose value == original to have value = replacement.
The function returns None.
'''
def ll_replace(head, original, replacement):
	curr = head
	while curr.next != None:
		if curr.value == original:
			curr.value = replacement
		curr = curr.next

	return None

 
def to_string(head): # to test your list
    parts, cur = [], head
    while cur:
        parts.append(str(cur.value))
        cur = cur.next
    return " -> ".join(parts) if parts else "EMPTY"

num3 = Node(5)
num2 = Node(6, num3)
num1 = Node(5, num2)
# initial linked list: 5 -> 6 -> 5
to_string(num1)

head = num1
ll_replace(head, 5, "banana")
to_string(num1)
# updated linked list: "banana" -> 6 -> "banana"

#Problem 6: List Nodes
'''
takes in a head of a linked list and a non-negative integer n as parameters.
The function returns a list of values of the first n nodes.
If n is greater than the length of the linked list, return a list of the values of all nodes in the linked list.
'''
def listify_first_n(head, n):
	curr = head
	i = 0
	lst = []
	while curr != None and i<n:
		lst.append(curr.value)
		i+=1
		curr = curr.next
	return lst
	

# linked list: a -> b -> c
c = Node('c')
b = Node('b', c)
head = Node('a', b)

lst = listify_first_n(head,2)
print(lst)

# linked list: j -> k -> l 
l = Node('l')
k = Node('k', l)
head2 = Node('j', k)
lst2 = listify_first_n(head2,5)
print(lst2)

#Problem 7: Insert Value
'''
takes in a head of a linked list, a value val, and an index i as parameters.
The function should insert a new Node with value val at index i of the linked list, then return the head of the linked list.
If i is greater than the length of the list, insert the new node at the end of the list.
'''
def ll_insert(head, val, i):
	new_node = Node(val)

# linked list: 3 -> 8 -> 12 -> 9
ll_insert(head, 20, 2)

# result linked list: 3 -> 8 -> 20 -> 12 -> 9