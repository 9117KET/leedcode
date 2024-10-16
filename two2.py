#function def that takes nums and returns results
def sum2(nums):
    #initialize the results that will store the elements that agrees to the property
    results=[]
    #use a for loop to traverse through the list of elements one after the other
    for num in nums:
        #getting the doubled of the element
        doubled = 2*num
        #checking if it does not end in a two and if that is the case then we append the number to the results array
        if doubled % 10 != 2:
            results.append(doubled) #appending
    return results #returning the results with all the nums that do not end in a two after multiplication
