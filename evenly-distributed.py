def evenlySpaced(a, b, c):
    # Sort the given numbers in ascending order
    sortedNumbers = sorted([a, b, c])

    # Calculate the differences between consecutive numbers
    diff1 = sortedNumbers[1] - sortedNumbers[0]
    diff2 = sortedNumbers[2] - sortedNumbers[1]

    if(diff1==diff2):
        return True
    else:
        return False
    
    # lastly, we can simply "return (diff1==diff2) at the end instead of the four line of code"
    # Return True if the differences are equal, otherwise False
    # return diff1 == diff2
    


