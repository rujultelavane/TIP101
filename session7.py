# ------------------------- two pointer method lecture 1 -------------------------
'''
U(M)PI(R)(E)
    MATCH
        - identify patterns you can see again and again
        - ds or alg
        - think of simple versions that you have seen before
    
    REVIEW
        - go over the solution again
   
    EVALUATE
        - make sure it meets reqs and handles edge cases

TWO POINTER TECHNIQUE
    - move toward/away form ea other
    - common scenarios:
        - searching
        - sorting
        - comparing elements
        - looking for summed local maxima/minima over a window
            - 
'''
# ------ instructor demo ------
'''
Given a string s, determine if it can become 
a palindrome by removing at most one character.
'''
#understand
'''
1. input a string
2. output a boolean
3. palindrome is the same backwards and forwards
4. modifying that classic palindrome to allow for one incorrect answer
'''

#match
'''
Questions:
    - Does this seem familiar? --> yes similar to palindrome
    - Are pointers useful here --> yes bc we are navigating thru data, step by step. we need to be in multple places at the same time
    - How many poitners do we need and where do they begin? --> 2, one at 0, len(s)-1
    - Are there any simpler solutions that come to mind that we can work from? --> classoc palindrome
'''

#plan
'''
1. given a string
1.5 set up our two pointers (left and right, front and final pos)
2. will implement the classic palindrome solution first
2.5 we will "wrap" (wrapper) or plug in helper funcs to add the complexity back in
    - wrapper: u put another class around it 
3. we need to allow for onle ONE invalid character. "aba" "abba" "abac" .... "abacc"
    maybe this will use our helper func
    scoot our pointers one to the right, and one to he left, but only one time. if either one is correct, we will return true
4. return final result
'''

def classic_palindrome(s, left, right): #helper function
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

print(classic_palindrome("abba", 0, 3))

def valid_palindrome(s):
    #pointers are the index for strings
    left = 0
    right = len(s)-1

    #we will iterate thru letters, if smth is wrong, we do our scoor where only 1 of the two choices needs to be valid
    while left < right:
        if s[left] == s[right]:
            #move them closer
            left += 1
            right -= 1
        else:
            #we will allow for scooting only ONCE.
            #we will perform normal palindrome checking on both segments.
            return classic_palindrome(s, left+1, right) or classic_palindrome(s, left, right-1)
    return True

############# BREAKOUT ROOM PRACTICE -- UNIT 4 #############
'''
Write a function is_prime() that takes in a positive integer n and 
returns True if it is a prime number and False otherwise. 
A prime number is a number greater than 1 that has no positive 
divisors other than 1 and itself.
'''
def is_prime(n):
    if n <= 1: 
        return False
    if n == 2:
        return True
    
    #if even is false
    if n % 2 == 0:
        return False
    
    x = 3
    while x<n:
        if n%x == 0: #divisible by x
            return False
        x+=2
    
    return True

print(is_prime(5))
print(is_prime(12))
print(is_prime(9))
    
'''
Write a function reverse_list() that takes in a list lst and returns elements of the list in reverse order. The list should be reversed in-place without using list slicing (e.g. lst[::-1]).

Instead, use the two-pointer approach, which is a common technique in which we initialize two variables (also called a pointer in this context) to track different indices or places in a list or string, then moves the pointers to point at new indices based on certain conditions. In the most common variation of the two-pointer approach, we initialize one variable to point at the beginning of a list and a second variable/pointer to point at the end of list. We then shift the pointers to move inwards through the list towards each other, until our problem is solved or the pointers reach the opposite ends of the list.
'''
def reverse_list(lst): #time: O(n)
    left = 0
    right = len(lst) -1

    while left < right:
        lst[left], lst[right] = lst[right], lst[left] #unpacking - assigning whats at the left to the right and viceversa
        
        left += 1
        right -= 1
    return lst


print(reverse_list([1, 2, 3, 4, 5]))

'''
Write a function that takes in an integer list nums as a parameter and moves 
all the even integers at the beginning of the list followed by all the odd integers. 
The function returns any list that satisfies this condition.
'''
def sort_array_by_parity(nums):
    left = 0
    right = len(nums)-1

    while left<right:
        if nums[left] %2 == 0: #its in the right spot
            left += 1
        elif nums[right] %2 != 0: #right spot
            right -= 1
        else: #both are out of place
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
    
    return nums

nums = [3,1,2,4]
nums2 = [0]
print(sort_array_by_parity(nums))
print(sort_array_by_parity(nums2))

'''
Write a function first_palindrome() that takes in a list of strings words as a parameter and returns the first 
palindromic string in the list. If there is no such string, return an empty string ""
'''
def first_palindrome(words):
    if(len(words) == 0):
        return ""
    for word in words: #check if every word is a palindrome
        if classic_palindrome(word, 0, len(word)-1): #call helper function used in lecture
            return word #if its a palindrome return it
    return ""

words = ["abc","car","ada","racecar","cool"]
palindrome1 = first_palindrome(words)
print(palindrome1)

words2 = ["abc","racecar","cool"]
palindrome2 = first_palindrome(words2)
print(palindrome2)

words3 = ["abc", "def", "ghi"]
palindrome3 = first_palindrome(words3)
print(palindrome3)