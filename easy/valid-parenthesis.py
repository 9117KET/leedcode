'''
For the valid parenthesis problem:
We use the stack data structure to keep track of the opening and closing brackets
If the character is an opening bracket then we push it onto the stack (add)
if the character is a corresponding closing bracket, we pop it off the stack (delete it)

Check if the stack is not empty and the top of the stack is the matching opening bracket. If so, pop the top of the stack.
Check if the stack is empty or the top of the stack is not the matching opening bracket return False

At the end of the iteration, if the stack is empty, return True (meaning that all opening brackets where matched and closed correctly)
If the stack is not empty, return False (meaning some opening brackets where not closed)

This uses the LIFO data structure
'''

class Solution:
    def isValid(self, s: str)-> bool:
        #Stack to keep track of opening brackets
        stack = []
        #Hash map for keeping track of mappings.
        mapping = {')':'(', '}':'{', ']':'['}
        #For every character in the expression
        for char in s:
            #If the character is a closing bracket
            if char in mapping:
                #pop he topmost element from the stack if it is not empty
                #Otherwise, assign a dummy value "#" that will keep track and will not match any bracket
                top_element = stack.pop() if stack else '#'

                #If the mapping for this bracket doesn't match the stack s top element, return False
                if mapping[char] != top_element:
                    return False
            else:
            #if it is an opening bracket, push it onto the stack
                stack.append(char)

        return not stack


'''
Time and space complexity is O(n) because the algorithm iterate through the string 's' once.

'''