#LECTURE NOTES
'''
UMPIRE METHOD
- UNDERSTAND
    - understand what's being asked w/ ?s
    - get basic sample input/output
    - find edge cases
    - tradeoffs (memory, performance, simplicity)
    - figure out first approach to optimize later
- MATCH
- PLAN
    - describe overall approach in engl
    - simple + clear steps
    - shows interviewer ur holistic
- IMPLEMENT
    - translate plan into code
- REVIEW
- EVALUATE
'''

'''
write a func above_threshold() that takes in a list of ints nums
and an integer threshold as parameters. the func iterates thru the 
original list and returns a new list containing only numbers that are 
greater than threshold

def above_threshold(nums, threshold):
    pass

input: lst = [8,2,13,11,4,10,14], threshold=10
output: [13,11,14]
'''
#PLAN

#create structure of our function, including input and output
#create a new list, which will be returned
#iterating through the list of nums, for loop
#if statement, checking against threshold
#return that new list

def above_threshold(nums, threshold):
    final_list = []

    for num in nums:
        if num > threshold:
            final_list.append(num)

    return final_list

print("Test run", above_threshold([8,2,13,11,4,10,14], 10))


############# BREAKOUT ROOM PRACTICE #############

#1.
def all_in(a,b):
    #For
    #iterate through list a
    #check (if statement) its also in b
    #if its not then return false

    for num in a:
        if num in b:
            continue
        else:
            return False
    return True

print("Problem 1: ", all_in([1, 2], [1, 2, 3]))


#2.
def create_dictionary(keys, values):
    #initialize an empty dictionary
    #iterate through keys and values(loop)
    #add a new key-value pair for each key-value

    d = {}
    for i in range(len(keys)):
        d[keys[i]] = values[i]

    return d

keys = ['peanut', 'dragon', 'star', 'pop', 'space']
values = ['butter', 'fly', 'fish', 'corn', 'ship']
print("Problem 2: ", create_dictionary(keys, values))

#3. 
def print_pair(dictionary, target):
    #loop through dictionary
    # if the key == target -> print it
    #if target not found, print it doesnt exist

    found = False
    for key in dictionary.keys():
        if key == target:
            print("Key: ", key, "\nValue: ", dictionary[key])
            found = True
    
    if not found:
        print("That pair does not exist!")

dictionary = {"spongebob": "squarepants", "patrick": "star", "squidward": "tentacles"}
print_pair(dictionary, "patrick")
print_pair(dictionary, "plankton")
print_pair(dictionary, "spongebob")

#4.
def keys_v_values(dictionary):
    #2 accumulator variables for the sums of keys and values
    #loop through the keys of dictionary (dictionary.keys())
        #add the key to sum
    #^^ do the same thing but for values
    sum_keys = 0
    for key in dictionary.keys():
        sum_keys += key
    
    sum_values = 0
    for value in dictionary.values():
        sum_values += value

    #compare the two
    if sum_keys > sum_values:
        return 'keys'
    elif sum_values > sum_keys:
        return 'values'
    else:
        return 'balanced'
    
dictionary1 = {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}
greater_sum = keys_v_values(dictionary1)
print(greater_sum)

dictionary2 = {100:10, 200:20, 300:30, 400:40, 500:50, 600:60}
greater_sum = keys_v_values(dictionary2)
print(greater_sum)

#5. 
def restock_inventory(current_inventory, restock_list):
    #loop through restock_list keys
    #add the value of the restock key to the corresponding current inventory key

    for restock_key in restock_list.keys():
        restock_value = restock_list[restock_key]

        if (restock_key in current_inventory):
            current_inventory[restock_key] += restock_value
        else:
            current_inventory[restock_key] = restock_value
    
    return current_inventory


current_inventory = {
    "apples": 30,
    "bananas": 15,
    "oranges": 10
}

restock_list = {
    "oranges": 20,
    "apples": 10,
    "pears": 5
}
print("Problem 5: ", restock_inventory(current_inventory, restock_list))

#6. 
def calculate_gpa(report_card):
    grades = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'F': 0 }
    #accumulator variable for total grade points
    #iterate through report card values
    #add to total grade points based on grades{}
    #find avg

    total_grade_points = 0
    for grade in report_card.values():
        total_grade_points += grades[grade]
    
    gpa = total_grade_points / len(report_card)
    return gpa

report_card = {"Math": "A", "Science": "C", "History": "A", "Art": "B", "English": "B", "Spanish": "A"}
print(calculate_gpa(report_card))

#7. 
def highest_rated(books):
    #returns the book with the highest rating
    #books is a list of dictionaries

    #variable highest to track the highest rating
    #loop thru each dictionary in books and get rating
    # if higher than highest, change highest to current book

    highest_book = {"rating": 0}
    for i in range(len(books)):
        current_book = books[i]
        rating = current_book["rating"]
        if rating > highest_book["rating"]:
            highest_book = books[i]
    
    return highest_book

books = [
    {"title": "Tomorrow, and Tomorrow, and Tomorrow",
     "author": "Gabrielle Zevin",
     "rating": 4.18
    },
    {"title": "A Fortune For Your Disaster",
     "author": "Hanif Abdurraqib",
     "rating": 4.47
    },
    {"title": "The Seven Husbands of Evenlyn Hugo",
     "author": "Taylor Jenkins Reid",
     "rating": 4.40
    }
]
print(highest_rated(books))

#8.
def index_to_value_map(lst):
    #create an empty dictionary
    #loop from 0-len(list)
    # i is the key, and lst[i] is the value

    d = {}
    for i in range(len(lst)):
        d[i] = lst[i]
    
    return d 

print(index_to_value_map(["apple", "banana", "cherry"]))