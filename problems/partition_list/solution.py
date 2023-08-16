# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        l_head = ListNode() # left < x
        r_head = ListNode() # right >= x
        cur, l, r = head, l_head, r_head

        while cur != None:
            nxt = cur.next
            if cur.val < x:
                l.next = cur
                l = l.next
                l.next = None
            else:
                r.next = cur
                r = r.next
                r.next = None
            cur = nxt

        l_head = l_head.next
        r_head = r_head.next

        l.next = r_head
        return l_head if l_head else r_head 
        
        