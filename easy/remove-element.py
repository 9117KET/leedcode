def removeElement(nums, val):
    #Create a variable to hold the pointer for the next position of the non-val element
    k = 0

    #Traverse through the array to search for all elements that are different from val and update our k
    for i in range(len(nums)):
        #if the current element is not equal to val, we place it at the current position of k
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k

