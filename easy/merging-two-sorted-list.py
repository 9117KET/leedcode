'''
In this question, we are given two sorted list l1 and list l2.
We need to merge the two into another another list which is sorted.
To solve this algorithm, we need to create a dummy variable that will help in handling the edge cases and acting as the head of our sorted list
create a current pointer that points to dummy variable.

'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        #Create a dummy node to handle the edge cases
        dummy = ListNode()
        current = dummy

        #Traverse both lists
        while list1 and list2:
            #Compare the value of the current node in both lists
            if list1.val<list2.val:
                #if this is true then the smaller value is from list1 then we attach the node to the merged list
                current.next=list1
                #Then move the list1 pointer to the next node
                list1=list1.next
            else:
                #this means the smaller value is from list2 meaning that our first if statement is false and we 
                #Change the current next node to be from list2
                current.next = list2
                #move the list2 pointer to the next node
                list2=list2.next

            #Then after the comparison, move our pointer to the merged list to the next node
            current = current.next

        # if for some reason, one of the list is exusted then simply attach the remaining nodes from either list 1 or list 2 to the merged list
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        #Return the head of the merged list, which starts at the dummy.next
        return dummy.next


    '''
    Time complexity: O(n+m)
    Space complexity: O(1)
    '''  

    #approach two
    class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: ListNode
        :type list2: ListNode
        :rtype: ListNode
        """
        # Base cases: if either list is empty, return the other list
        if not list1:
            return list2
        if not list2:
            return list1
        
        # Recursive case: merge the smaller node and recursively merge the rest
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
