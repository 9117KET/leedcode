'''
In this problem, we have been given a roman numerial and we are suppose to return the equivalent integer value 
following the roman numerial rules like
- If a smaller number appear before a larger one, we subtract the two
- If a larger number appear before a smaller one, we add the two

To solve this problem, we can use a dictionary to store the values of the roman numerals and their corresponding integer values.
We can then iterate through the string using a for loop and use the dictionary to get the integer value of the roman numeral.
We also need to keep track of the previous numeral we have seen so that we can determine if we need to add or subtract the current numeral.

'''
class Solution(object):
    def romanToInt(self, s):
        '''
        :type s: str
        :rtype: int
        '''
        # Dictionary mapping Roman numerals to integers
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0  # Initialize the total value to 0
        prev_value = 0  # Variable to store the value of the previous numeral

        # Loop through each character in the string
        for numeral in s:
            value = roman_to_int[numeral]  # Convert the Roman numeral to its integer value

            # Check if the previous numeral is less than the current numeral
            if prev_value < value:
                # Subtract twice the previous value because it was added once before
                total += value - 2 * prev_value
            else:
                # Add the value of the current numeral to the total
                total += value

            prev_value = value  # Update the previous numeral value

        return total
    

#a more optimize memory solution is

class Solution(object):
    def romanToInt(self, s):
        roman_to_int = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

        total = 0
        prev_value = 0

        # Convert string to list of values using tuple unpacking
        values = [roman_to_int[numeral] for numeral in s]

        for value in values:
            if prev_value < value:
                total += value - 2 * prev_value
            else:
                total += value
            prev_value = value

        return total

