# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ##### Time O(2n) | Space O(1) #####
        # edge cases
        # if head.next == None:
        #     return None
        # if head.next.next == None:
        #     if n == 1:
        #         head.next = None
        #         return head
        #     else:
        #         head = head.next
        #         return head
        if n == 1:
            tail = self.reverse(head)
            tail = tail.next
            return self.reverse(tail)
        
        # reverse linked list
        tail = self.reverse(head)
    
        # find n-1 th node from end of linked list
        pt = tail
        for i in range(1, n-1):
            pt = pt.next
               
        # remove nth node from end of linked list
        tmp = pt.next.next
        pt.next.next = None
        pt.next = tmp
                
        # reverse linked list again
        return self.reverse(tail)
        
    def reverse(self, head):
        # reverse linked list
        prev, cur = None, head
        while cur != None:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        return prev
        