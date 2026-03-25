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


############# BREAKOUT ROOM PRACTICE -- UNIT 5 #############
#Version 3

from collections import Counter
class Player():
    def  __init__(self, character, kart):
        self.character = character
        self.kart = kart
        self.items = []
    def get_player(self):
        return f"{self.character} driving the {self.kart}"
    def set_player(self, name):
        names = ["Mario", "Luigi", "Peach", "Yoshi", "Toad", "Wario", "Donkey Kong", "Bowser"]
        if name in names:
            self.character = name
            print("Character Updated")
        else:
            print("Invalid name")
    def add_item(self, item_name):
        valid_items = ["banana", "green shell", "red shell", "bob-omb", "super star", "lightning", "bullet bill"] 
        if item_name in valid_items:
            self.items.append(item_name)
    def print_inventory(self):
        if len(self.items) == 0:
            print("Inventory empty")
            
        inventory = dict(Counter(self.items))
        for item, quantity in inventory.items():
            print(f"{item}: {quantity}", end= ",")
    def print_results(race_results):
        i = 1
        for character in race_results:
                print(f"{i}. {character.character}")
                i+=1


    
#2.
#Create a second instance of Player in a variable named player_two.
#The Player object created should have character "Bowser" and kart "Pirahna Prowler".
#Step 3: Use the method get_player() below to print out "Match: Yoshi driving the Super Blooper vs Bowser driving the Pirahna Prowler"
player_one = Player("Yoshi", "Super Blooper")
player_two = Player("Bowser", "Pirahna Prowler")
print(f"{player_one.get_player()} vs {player_two.get_player()}")

#3. Update player_one so that their kart is "Dolphin Dasher" instead of it's current value, "Super Blooper".
print(player_one.get_player())
player_one.kart = "Dolphin Dasher"
print(player_one.get_player())


player_one.set_player("Peach")
player_two.set_player("Kermit")

#4.
'''
Players can pick up special items as they race.

Update the Player class with a new method add_item() that takes in one parameter, item_name.

The method should validate the item_name.

If the item is valid, add item_name to the player’s items attribute.
The method does not need to return any values.
item_name is valid if it has one of the following values: "banana", "green shell", "red shell", "bob-omb", "super star", "lightning", "bullet bill".
'''
player_one.add_item("red shell")
# items = ["red shell"]
player_one.add_item("super star")
# items = ["red shell", "super star"]
player_one.add_item("super smash")
# items = ["red shell", "super star"]

print(player_one.items)

#6
player_one = Player("Yoshi", "Super Blooper")
player_one.items = ["banana", "bob-omb", "banana", "super star"]
player_two = Player("Peach", "Dolphin Dasher")

player_one.print_inventory()
player_two.print_inventory()