def evenlySpaced(a,b,c):
    #sorted the given numbers in ascending order
    sortedNumbers = ([a,b,c]);

    #Calculate the difference using their index position
    diff1=sortedNumbers[0]-sortedNumbers[1]
    diff2=sortedNumbers[2]-sortedNumbers[1]

    if(diff1==diff2):
        return True
    else:
        return False
    
    #lastly, we can simply "return (diff1==diff2) at the end instead of the four line of code"
    


