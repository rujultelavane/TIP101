#instructor demo

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

