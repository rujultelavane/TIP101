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

############# BREAKOUT ROOM PRACTICE -- UNIT 3 #############
#1.
def match_made(dictionary):
    for key, value in dictionary.items():
        print( f"{key} and {value} are a perfect match.")

names ={
    'Peanut butter': 'Jelly',
    'Spongebob' : "Patrick",
    'Ash':'Pikachu'
}

match_made(names)

#2. 
def remove_char(s, n):
    s = s[:n] + s[n+1:]
    print(s)
    
remove_char("typpo", 2)

#3.
def vowel_count(s):
    vow="aeiouyAEIOUY"
    count=0
    for char in s:
        if char in vow:
            count+=1
    return count

my_str = "hello world"
my_str2 = "aAaAaAaAAA"
my_str3 = "ths strng s mssng vwls"
print(vowel_count(my_str))
print(vowel_count(my_str2))
print(vowel_count(my_str3))

#4. 
def reverse_sentence(sentence):
    lst = sentence.split(" ")
    lst.reverse()
    return " ".join(lst)

sentence = "I solemnly swear I am up to no good"
print(reverse_sentence(sentence))

#5.
def compress_string(my_str):
    stack = []
    res = ""
    for ch in my_str:
        if ch in stack or len(stack)==0:
            stack.append(ch)
        else:
            res += f"{stack.pop()}{len(stack)+1}"
            stack = []
            stack.append(ch)
    for ch in stack:
        res += f"{stack.pop()}{len(stack)+1}"
    print(res)
    
compress_string("aaaaabbcccd")

#6.
def find_the_needle(haystack, needle):
    if needle in haystack:
        return haystack.index(needle)
    else:
        return -1

haystack = "tobeornottobe"
needle = "be"
print(find_the_needle(haystack, needle))

haystack2 = "leetcode"
needle2 = "leeto"
print(find_the_needle(haystack2, needle2))