def strStr(haystack, needle):
    #edge case
    if needle == "":
        return 0
    
    #iterate through the haystack stopping early if remaining characters are less than needle
    for i in range(len(haystack) - len(needle) + 1):
        # checking if the substring matches needle
        if haystack [i:i + len(needle)] == needle:
            return i
    # if needle is not found in haystack.
    return -1
"""
Further explanation 
i:i + len(needle): This is a slice notation in Python that extracts a portion of the haystack 
string starting at index i and ending at index i + len(needle).
"""