def wordCount(s):
    # Initialize a count variable to keep track of matching patterns
    count = 0
    # Iterate through the string up to the last possible starting index for a four-character word
    for i in range(len(s)-3):
        # Check if the current slice of four characters starts with 'co' and ends with 'e'
        # This checks for a pattern like 'code' where there is exactly one character between 'co' and 'e'
        if s[i:i+2] == 'co' and s[i+3] == 'e':
            count += 1  # Increment count if the pattern is found
    return count

'''
if s[i:i+2] == 'co' and s[i+3] == 'e':
This line checks if the substring starting from index i and spanning two characters equals "co" (s[i:i+2] == 'co').
It also checks if the character exactly two positions after the "co" is an 'e' (s[i+3] == 'e').
'''