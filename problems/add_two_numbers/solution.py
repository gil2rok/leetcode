# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = ListNode()
        carry = 0
        
        p1 = l1
        p2 = l2
        p3 = l3
        
        while p1.next != None and p2.next != None:
            p3.val = (p1.val + p2.val + carry) % 10
            carry = (p1.val + p2.val + carry) >= 10
            
            p3.next = ListNode()
            
            p1 = p1.next
            p2 = p2.next
            p3 = p3.next
        
        p3.val = (p1.val + p2.val + carry) % 10
        carry = (p1.val + p2.val + carry) >= 10
        
        while p1.next != None:
            p3.next = ListNode()
            p3 = p3.next
            p1 = p1.next
            
            p3.val = (p1.val + carry) % 10
            carry = (p1.val + carry) >= 10
           
        while p2.next != None:
            p3.next = ListNode()
            p3 = p3.next
            p2 = p2.next
            
            p3.val = (p2.val + carry) % 10
            carry = (p2.val + carry) >= 10

        if carry == 1:
            p3.next = ListNode()
            p3 = p3.next
            p3.val = 1
            
        return l3
 