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
'''
create structure of our function, including input and output
create a new list, which will be returned
iterating through the list of nums, for loop
if statement, checking against threshold
return that new list
'''
def above_threshold(nums, threshold):
    final_list = []

    for num in nums:
        if num > threshold:
            final_list.append(num)

    return final_list

print("Test run", above_threshold([8,2,13,11,4,10,14], 10))