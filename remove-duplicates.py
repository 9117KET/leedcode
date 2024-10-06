def removeDuplicates(nums):
    #edge case
    if not nums:
        return 0
    
    # we initialize the first pointer to point to the unique element
    i = 0

    # iterate through the array starting from the second element
    for j in range (1, len(nums)):
        if nums[j]!=nums[i]: # this means we have found a new unique element
            # we move the i pointer to the next position
            i += 1
            #update it with a new unique element
            nums[i]=nums[j]

    # return the length of the array with unique elements
    return i+1