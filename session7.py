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
            return classic_palindrome(s, left+=1, right) or classic_palindrome(s, left, right-=1)
    return True

    #implement palindrome logic
    
    # while left<right