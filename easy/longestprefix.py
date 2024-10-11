class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        #handling edge case
        if not strs:
            return ""
        
        # Start with the first string as the prefix
        prefix = strs[0]
        
        #We then compare the prefix with each string in the list
        for string in strs[1:]:
            # Keep shorting the prefix until it matches the beginning of the string
            while not string.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
            #The while loop continues as long as the current string doesn't start with the prefix
            #if the current string doesn't start with the prefix, we progressively shorten prefix by removing its last character (prefix = prefix[-1])
        return prefix