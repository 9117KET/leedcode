#function definition with input parameter
def scoreClump(scores):
    #iterating through the list, considering each group of three consecutive scores
    for i in range(len(scores)-2):
        #extract the three scores into a list
        clump = scores[i:i+3]
        #check if the difference between the maximum and minimum scores in the clump is less than or equal to 2
        if max(clump) - min(clump) <= 2:
            return True
    return False
