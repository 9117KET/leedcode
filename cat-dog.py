"""
This module defines a function that checks if the substrings "cat" and "dog" appear the same number of times in a given string.

Examples:
- cat_dog('catdog') returns True because "cat" and "dog" both appear once.
- cat_dog('catcat') returns False because "cat" appears twice, but "dog" does not appear.
- cat_dog('1cat1cadodog') returns True because both "cat" and "dog" appear once amidst other characters.
"""

def cat_dog(s):
    # Initialize counters for "cat" and "dog" occurrences
    count_cat = 0
    count_dog = 0
    
    # Iterate through the string, checking every substring of length 3
    for i in range(len(s) - 2):  # Stop at len(s) - 2 to avoid out-of-bounds error
        # Check if the current 3-character window is "cat"
        if s[i : i + 3] == 'cat':
            count_cat += 1
        # Check if the current 3-character window is "dog"
        elif s[i : i + 3] == 'dog':
            count_dog += 1
    
    # Return True if "cat" and "dog" are found the same number of times
    return count_cat == count_dog
