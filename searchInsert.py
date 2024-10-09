def searchInsert(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        #if the target is found, return its index
        if nums[mid] == target:
            return mid
        #if the target is larger, search in the right half
        elif nums[mid] < target:
            left = mid + 1
        #if the target is smaller, search in the left half
        else:
            right = mid - 1

    # if the target is not found, return the insertion point (left)
    return left

'''
left = 0:

This initializes the left pointer to the first index of the array nums. In Python, array indexing starts at 0, so the first element is at index 0. 
This means that the binary search will start considering the range from the very beginning of the array.
right = len(nums) - 1:

right is initialized to the last index of the array. len(nums) gives the total number of elements in the array, but since array indexing starts at 0, 
the last element is located at len(nums) - 1.
For example, if the array has 5 elements, len(nums) would be 5, and the last index would be 5 - 1 = 4.
'''

'''
nums = [1, 3, 5, 6]
target = 5

Step-by-Step Walkthrough:
Initialization:

The input array is nums = [1, 3, 5, 6].
The target value is target = 5.
Left pointer (left) is initialized to 0 (the start of the array).
Right pointer (right) is initialized to 3 (the last index of the array, which is len(nums) - 1 = 3).

left = 0, right = 3

First Iteration of the While Loop:
The condition left <= right is checked. Since 0 <= 3 is True, the loop proceeds.
Middle index (mid) is calculated as

mid = (left + right) // 2
    = (0 + 3) // 2
    = 1

    
Now, check nums[mid]:
nums[mid] = nums[1] = 3.
Compare nums[mid] with target:
nums[mid] (3) < target (5).
Since nums[mid] is less than target, update the left pointer

left = mid + 1
    = 1 + 1
    = 2

    
left = 2, right = 3
Second Iteration of the While Loop:

The condition left <= right is checked. Since 2 <= 3 is True, the loop proceeds.
Middle index (mid) is calculated as

mid = (left + right) // 2
    = (2 + 3) // 2
    = 2


Now, check nums[mid]:
nums[mid] = nums[2] = 5.
Compare nums[mid] with target:
nums[mid] (5) == target (5).
Since nums[mid] equals the target, we return mid:

return mid  # returns 2

'''