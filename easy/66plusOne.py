class Solution(object):
    def plusOne(self, digits):
        '''
        :type digits: List[int]
        :rtype: List[int]
        '''
        #Start from the last digit and traverse backwards
        for i in reversed(range(len(digits))):
            # if the current digit is less than 9, simply add 1 and return the results
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # Otherwise, set the current digit to 0 and move to the next digit
            digits[i] = 0

        #If the loop completes, it means all digits were 9 (e.g., 999->1000)
        #Therefore, we will add a new leading 1 to the front
        return [1] + digits
    
    """
    Example 1 work through
    input: digits = [1, 2, 3]

    Start from the last digit, which is 3 from line 8
    add 1 to 3 to get 4 from line 10 and 11
    return the modified array [1,2,4] from line 12

    Example 2 work through
    input: digits = [9, 9, 9]
    in this case, the if condition doesn't hold so all the digits (999) will be transform into 0(s)

    return [1]+digits from line 14 and 18. 
    Just like  in primary school, when we have 9, we carry over to the next digit.

        Start from the last digit, which is 9.
        Add 1 to 9, making it 10. Set the current digit to 0 and carry over to the next digit.
        Repeat for the second and first digits (both 9), turning the array into [0, 0, 0].
        Since all digits were 9, prepend 1 to the array and return [1, 0, 0, 0].


    Time and Space complexity
    Time complexity: O(n)
    Space complexity: O(1) or O(n) if we include the extra space required when adding a new digit.
    """