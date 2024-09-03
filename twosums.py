# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.


#Method 1: Brute Force
#Use two nested loops to iterate through the array and check through all possible pairs of numbers in the list.
#For each pair, check if the sum of the two numbers equals th target
#If a pair is found, return the indices of the two numbers,

def two_sum(nums, target):
    #Iterate through each element in the list
    for i in range(len(nums)):
        #Iterating through the the remaining elements after the current element
        for j in range(i+1, len(nums)):
            #Check if the current pair adds up to the target
            if nums[i] + nums[j] == target:
                #return the indices of the two numbers
                return [i, j]
#Time complexity: O(n^2)
#Space complexity: O(1)


#Method 2: Hash Map
#Create a dictionary called `num_to_index` to store the numbers as keys and their corresponding indices as values.
#Iterate through the list once
#For each element `num` in the list at index `i`, calculate the `complement` which is `target` minus `num`. 
#Check if the complement is already in the dictionary `num_to_index`.
#If it is, return the indices of the current number and its complement.
#If it is not found, add `num` to the dictionary `num` to the dictionary with its index as the value.
#continue the loop until the solution is found.

def two_sum(nums, target):
    #Create a dictionary to store the numbers and their indices
    num_to_index = {}

    #Iterate through the list
    for i, num in enumerate(nums):
        #calculate the complement that would sum to the target
        complement = target - num
        #Check if the complement exists in the dictionary
        if complement in num_to_index:
            #if found, return the indices of the current number and its complement
            return [num_to_index[complement], i]
        
        #Otherwise, add the current number and its index to the dictionary
        num_to_index[num] = i


#Time complexity: O(n)
#Space complexity: O(n)


#Application of the two-sum problem.
'''
Financial Transaction and fraud detection:
- in real life, one might need to detect a fraudulent transaction by looking at the sum of the transaction that leads to the specific suspicious amount.

Inventory management and budgeting
- A company might need to manage its inventory by keeping track of the quantities of different items.

Gift Card or coupon code business
- And e-commerce website might issue gift cards or coupon codes to customers that sum up to the exact balance of the gift card or coupon code, Temu uses this all the time.

Pairing task in project management
-In project management, one might need to pair tasks to employees based on their skills and availability such that the sum of the available task matches their work shift.

'''