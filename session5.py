#.replace()
sample4 = "This is our samplessssss fourth sample string for the day."
print(sample4.replace(" sample ","REPLACED"))

#slicing --> allows us to extract (parse) snippets of the text out.
sample5 = "This is our fifth sample string for the day."
print(sample5[0]) #prints letter at index 0
print(sample5[:5]) #prints everything up till 5
print(sample5[0:]) #prints whole string
print(sample5[0:10:2]) #gives first 10 characters, every other

#instructor demo
#understand
'''is pangram
 - all letters present at least one time
 - input: string, any case
 - return: boolean T/F
'''

#plan - hint: python has a built in function, isalpha() that might help
'''
1. working with unknown size string - clean up the string to know the expected format
2. wanna check for all 26 letters using a dictionary
2.5 we need to use a for loop to iterate thru each char
    - key -> letter, value -> true/false
3. count # keys in dictionary, if == 26, (return value)
'''
def is_pangram(sentence):
    lowercase_sentence = sentence.lower()
    letter_appearances = {} #key letter, value T/F

    for char in lowercase_sentence:
        if char.isalpha() == False:
            pass #pass == ignore, continue == jump to next iteration
        if char not in letter_appearances: #first time seeing it
            letter_appearances[char] = True
    
    if(len(letter_appearances) == 26):
        return True
    else:
        return False

inputSample = "The quick brown fox jumps over the lazy dog."
