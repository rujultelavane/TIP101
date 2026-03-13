# ------------------------- strings lecture 2 -------------------------
'''
strings are immutable!
useful methods: .lower(), .upper(), .split(), .replace()
formatting: print(f"{} blah blah blah")
'''
userName = "Rujul2026"
currentTime = "March 12th, 8:10pm"
#old way (concatenation)
#print(userName + "has signed in at" + currentTime) 
#approach 1
print(f"{userName} has signed in at {currentTime}")
#approach 2
print("{} has signed in at {}".format(userName, currentTime))

# ------------------------- instructor demo -------------------------
'''
Given a string s containing words separated by spaces, 
reverse the order of the words. Remove extra spaces 
and ensure that words are separated by a single space 
in the output. 
'''
def reverse_words(s):
    '''
    break up the words into individual components
    reverse them somehow
    glue the words bac together in reverse order, adding spacing back in.
    return the final string
    '''
    word_list = s.split() #split by default--at every space.
    word_list.reverse()
    ",".join(word_list)

s = " the sky is  blue  "
#expected output: "blue is sky the"
print(reverse_words(s))

############# BREAKOUT ROOM PRACTICE -- UNIT 3 #############

#problem set 2, #5
'''
Write a function partition_labels() that takes in a string s as a 
parameter. s consists of lowercase letters and represents the order 
of characters as they appear in a document. The function partitions 
s into as many parts as possible so that each unique letter appears 
in at most one part, and returns a list of integers representing the 
size of these parts.
'''
def partition_label(s):
    has_char = {}
    
    for i in range(len(s)):
        has_char[s[i]] = i
        
    result = []
    start = 0
    end = 0
    
    for i in range(len(s)):
        char = s[i]
        
        if has_char[char] > end:
            end = has_char[char]
        
        if i == end:
            size = end - start + 1
            result.append(size)
            start = i + 1
    return result
        


s1 = "ababcbacadefegdehijhklij"
print(partition_label(s1))

s2 = "abcabcbadefffeda"
print(partition_label(s2))

#problem set 2, #6
'''
Write a function interleave_lists() that accepts two lists as parameters. 
The function should return a new list that combines the given lists by 
alternating which list it takes its next element from. It will take 
elements in order, and if one list is longer it will append the remaining
elements to the end of the interleaved list.
'''
#understand:
#input: two lists of integers
#output: new interwoven list that alternates between the input lists
#edge case: account for different sized lists

#plan:
#increment variable, take value of lst1 and add to interleave list
# if list length is less than i, don't access element in list at i
# else, append element at position i in list to interleave_list
# return interleave_list

def interleave_lists(lst1, lst2):
    interleave_list = []
    smallerList = []
    biggerList = []
    if len(lst1) < len(lst2):
        smallerList = lst1
        biggerList = lst2
    else:
        smallerList = lst2
        biggerList = lst1
    
    for i in range(len(biggerList)):
        #interleave_list.append(smallerList[i])
        interleave_list.append(biggerList[i])
        
        if i<len(smallerList):
            interleave_list.append(smallerList[i])
        
        '''if i >= len(smallerList):
            interleave_list.append(biggerList[i])'''
        
    #interleave_list.append(biggerList[len(smallerList):])
        
    return interleave_list
    
lst1 = [1, 2, 3, 4]
lst2 = [10, 20]
inter_lst = interleave_lists(lst1, lst2)
print(inter_lst)

#problem set 3 #1
'''
Write a function remove_vowels() that takes in a string s as a 
parameter and returns a new string with all the vowels removed. 
For the purposes of this exercise, consider a, e, i, o, and u 
as vowels and not y. The function should preserve the case of 
the original letters.
'''
def remove_vowels(s):
    new_string = ""
    vowels = "aeiou"
    for char in s:
        if char not in vowels:
            new_string += char
    
    return new_string

