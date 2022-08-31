# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        # find middle
        slow, fast = head, head
        while fast != None and fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
        
        # separate into two lists
        second = slow.next
        slow.next = None
        
        # reverse second list
        prev = None
        while second != None:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        # merge lists
        first, second = head, prev
        while first != None and second != None:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            
            first = tmp1
            second = tmp2
        
        
        
       
        
#         ##### Time O(n) | Space O(n) #####
#         loc = dict() # idx in linked list : node
#         idx = 0
#         pt = head
        
#         # add all elements to loc dict
#         while pt != None:
#             loc[idx] = pt
#             pt = pt.next
#             idx += 1
        
#         # while l, r pointers have not met 
#         l, r, = 0, idx-1 # considering even and odd length linked lists
#         while l + 1 < r:
            
#             # redirect pointers in list
#             loc[r-1].next = None
#             loc[r].next = loc[l+1]
#             loc[l].next = loc[r]
            
#             # increment l, r pointers
#             l += 1
#             r -= 1