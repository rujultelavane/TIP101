#DICTIONARIES LECTURE 2
# ------------------------- instructor demo -------------------------
#when to use lists/dictionaries:
'''
lists:
    ordered data
    keeping data in chronological order
    arrival time matters (first come first served)
    size expected to be constant

dictionaries:  
    key-value mapping
    dynamically grows
    speed prioritized
    unknown keys (user input)
'''
'''
# Understand:
    given list of tuples, where each tuple has a category and value
    write a func to count how many items belong to each category
    input: tuples, always same size, 0 category, 1 value (item)
    output: dictionary, keys categories, values will be the count

    Input: items = [("fruits", "apple"), ("vegetables", "carrot"), ("fruits", "banana")]
    Output: {"fruits": 2, "vegetables": 1}


#Plan:
    1. initialize out count_dictionary{}
    2. for loop, iterate through our list of tuples
        - 2a. parse out the item contents (category, name)
        - 2b. implement our count logic
    3. return count_dicitonary
'''
def count_by_category(items):
    count_dictionary = {} #starts empty, keys: category, values: count

    for item in items:
        #item is a tuple
        current_category = item[0]
        current_name = item[1]

        if current_category not in count_dictionary:
            #its the first time we are seeing it
            count_dictionary[current_category] = 1
        else:
            #weve seen it before
            count_dictionary[current_category] += 1
    
    return count_dictionary

#Test it
test_items = [("fruits", "apple"), ("vegetables", "carrot"), ("fruits", "banana")]
print(count_by_category(test_items))

############# BREAKOUT ROOM PRACTICE -- UNIT 3 #############
#Session 1 version 1
#1.
'''swapping first and last letters
takes in string '''

def swap_ends(my_str):
    res = my_str[-1] + my_str[1:-1] + my_str[0]
    return res

my_str = "boat"
swapped = swap_ends(my_str)
print(swapped)

#2.
def is_pangram(my_str):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    my_str = my_str.lower()

    for letter in alpha: #check every letter in alpha
        if letter not in my_str: #if not in the string then it's false
            return False
    return True

my_str = "The quick brown fox jumps over the lazy dog"
print(is_pangram(my_str))

str2 = "The dog jumped"
print(is_pangram(str2))

#3. reverse the whole string
def reverse_string(my_str):
    result_str = ""
    for i in range(len(my_str)-1,-1,-1):
        result_str += my_str[i]

    return result_str

#4. finds first non-repeating char
def first_unique_char(my_str):
    counts = {}
    for char in my_str:
        if char not in counts:
            counts[char] = 1
        else:
            counts[char] += 1
    
    for index in range(len(my_str)):
        char = my_str[index]
        if counts[char] == 1:
            return index
    
    return -1

my_str = "leetcode"
print(first_unique_char(my_str))

str2 = "loveleetcode"
print(first_unique_char(str2))

str3 = "aabb"
print(first_unique_char(str3))

#5. gets distance between words in a sentence
def min_distance(words, word1, word2):
    num1, num2 = 0, 0
    for k, v in enumerate(words): #enumerate -- get counter and item at the same time
        if v == word1:
            num1 = k
        elif v == word2:
            num2 = k
    
    return (num2-num1) if num2>num1 else (num1-num2)

words = ["the", "quick", "brown", "fox", "jumped", "the"]
dist1 = min_distance(words, "quick", "jumped")
dist2 = min_distance(words, "the", "jumped")
print(dist1)
print(dist2)

words2 = ["code", "path", "code", "contribute",  "practice"]
dist3 = min_distance(words2, "code", "practice")
print(dist3)