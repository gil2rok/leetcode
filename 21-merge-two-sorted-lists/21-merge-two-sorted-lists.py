# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # edge case if list1 or list2 is empty
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        
        # init head and pointer
        if list1.val > list2.val:
            head, pt = list2, list2
            list2 = list2.next
        else:
            head, pt = list1, list1
            list1 = list1.next
            
        n1, n2 = list1, list2
        
        # while not reached end of list1 AND list2
        while n1 != None and n2 != None:
            if n1.val >= n2.val:
                pt.next = n2
                pt = pt.next
                n2 = n2.next
            else:
                pt.next = n1
                pt = pt.next
                n1 = n1.next
            
        # add all remaining elements of list1
        while n1 != None:
            pt.next = n1
            pt = pt.next
            n1 = n1.next
        
        # add all remaining elements of list2
        while n2 != None:
            pt.next = n2
            pt = pt.next
            n2 = n2.next
        return head
        