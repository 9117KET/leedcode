def lengthOfLastWord(s):

    #Initialize a counter for the length of the last  word.
    length = 0

    #Start fro the end of the string and traverse backward
    for i in reversed(s):
        if i != ' ': #meaning that if the character is not a space, count it
            length += 1
        elif length > 0: #if a space is encountered after counting a word, break.
            break
    return length

'''
s = "Hello World I am Kinlo"

Detailed Explanation for Each Character:
First character ('o'): It is not a space, so we increase the length by 1 (length = 1).
Second character ('l'): It is not a space, so we increase the length by 1 (length = 2).
Third character ('n'): It is not a space, so we increase the length by 1 (length = 3).
Fourth character ('i'): It is not a space, so we increase the length by 1 (length = 4).
Fifth character ('K'): It is not a space, so we increase the length by 1 (length = 5).
Sixth character (' ') (space): We encounter a space, but since length > 0 (we have already counted the last word), we stop and break out of the loop.
'''