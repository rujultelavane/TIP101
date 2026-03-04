#DICTIONARIES LECTURE
'''
 - lowkey #1 way to optimize algo
 - key-value pairs
 - not in certain order
 - O(1) lookup
 - common uses
    - frequency maps (includes does it exist)
    - key-value data storage (data for 1-1 lookups)
'''

'''INSTRUCTOR LED EXAMPLE
anagrams (given list words, group the strings that are anagrams of each other)'''

def group_anagrams(words):
    '''
    #1. takes in a list of words
    #2. we will make a new dictionary (starting empty) -- thigns need to be associated with each other, sounds like key-value
    #3. iterate through the original list (for loop)
    #4. check if the current word is an anagram of something else
    #4b. figure how to assess anagrams
            - a signature (put the word in alphabetic order)
                eat -> aet
                tea -> aet
                ate -> aet
    #5. keep track/update our dictionary with new decisions
    #6. return a list
    '''
    anagram_dictionary = {} #aet -> [tea, eat, ate]

    for word in words:
        sorted_word = str(sorted(word))  #tea -> aet

        if sorted_word not in anagram_dictionary: #if thing is in dictionary
            anagram_dictionary[sorted_word] = [word] #make sure value is a list
        else: #else if thing is not in dictionary
            anagram_dictionary[sorted_word].append(word)
    
    return list(anagram_dictionary.values()) #you want to return the list, not the entire dictionary

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
#expected: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
print(group_anagrams(words))