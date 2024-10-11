class Solution(object):
    def isPalindrome(self, x):
        '''
        :type x: int
        :rtype: bool
        '''
        # Dealing with edge cases, ie, negative numbers and numbers ending in 0
        if x < 0 or (x > 0 and x % 10 == 0):
            return False
        
        # Initialize the reversed half of the number
        reversed_number = 0

        # Reverse the second half of the number using a while loop
        while x > reversed_number:

            # Extract the last digit of x and add it to the reversed half
            reversed_number = reversed_number * 10 + x % 10

            # Remove the last digit from x
            x = x // 10

        # Check if the number is a palindrome
        # If the number has is even, x should be equal to reversed_half
        # If the number has is odd, x should be equal to reversed_half // 10
        return x == reversed_number or x == reversed_number // 10
    
    '''
    Note that all negative number are not palindromes
    All numbers ending in 0 are not palindromes unless the number is 0 itself which our code correctly identifies

    Time Complexity: O(log10(x))
    Space Complexity: O(1)
    
    Explanation:
    The time complexity is O(log10(x)) because we are essentially halving the number x in each iteration of the while loop.
    We start with the rightmost digit and construct the reversed number by multiplying the current reversed number by 10 and adding the last digit of x.
    This process continues until x is less than or equal to the reversed number, at which point we have reversed the second half of the digits.

    The number of digits in a positive integer n is given by d = floor(log10(n)) + 1.
    In the worst case, we need to process half of the digits in the number, which is floor(d/2).
    Since d = floor(log10(n)) + 1, we can express the time complexity as O(log10(n)).

    Example:
    n = 123 has log10(123) ≈ 2.09, and floor(2.09) + 1 = 3 digits.
    We process half of the digits, which is floor(3/2) = 1 digit.

    n = 12321 has log10(12321) ≈ 4.09, and floor(4.09) + 1 = 5 digits.
    We process half of the digits, which is floor(5/2) = 2 digits.
    '''
        
        
        
        