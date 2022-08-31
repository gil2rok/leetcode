# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ##### Time O(n) | Space O(n) #####
        # init loc dict and idx variable
        loc = [] # node index --> node
        idx = 0
        
        # fill dict with nodes and their indexes!
        pt = head
        while pt != None:
            loc.append(pt)
            pt = pt.next
            idx += 1
        
        # edge cases
        if idx == 1:  # idx is now equal to length of linked list
            return None
        if n == 1:
            loc[(-n) - 1].next = None
            return head
        if n == idx:
            return head.next
        
            
        # remove nth node from end of linked list
        loc[(-n) - 1].next = loc[((-n) + 1)]
        return head
        
#         ##### Time O(2n) | Space O(1) #####
#         # edge case
#         if n == 1:
#             tail = self.reverse(head)
#             tail = tail.next
#             return self.reverse(tail)
        
#         # reverse linked list
#         tail = self.reverse(head)
    
#         # find n-1 th node from end of linked list
#         pt = tail
#         for i in range(1, n-1):
#             pt = pt.next
               
#         # remove nth node from end of linked list
#         tmp = pt.next.next
#         pt.next.next = None
#         pt.next = tmp
                
#         # reverse linked list again
#         return self.reverse(tail)
        
    def reverse(self, head):
        # reverse linked list
        prev, cur = None, head
        
        while cur != None:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
            
        return prev
        