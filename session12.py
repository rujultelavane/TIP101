#MOCK INTERVIEW DAY -- NO LECTURE!

#breakout room work

'''
1. Given a string, return True if it is a nesting of zero or more pairs 
of parentheses. Return False otherwise. A valid pair of parentheses is 
defined as (). The input string will only contain the characters ( or ). 
Your solution must be recursive.
Evaluate the time and space complexity of your solution.
'''
def is_nested(s):
	if len(s) == 0:
		return True
	if(len(s)%2 != 0):
		return False
	
	if s[0]=="(" and s[-1]==")":
		return is_nested(s[1:-1])
	return False

print(is_nested("(())"))

#this one took a long time actually to get so that's all for today's session :)