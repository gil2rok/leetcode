# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    ##### Time O(m+n) | Space O(1) #####
    # m = len(l1), n = len(l2)
    # space does not include required output
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        res = ListNode()
        
        # add up numbers in both list1 and list2
        p1, p2 = l1, l2
        dummy = res
        while p1 != None and p2 != None:
            # create new node
            digit = (p1.val + p2.val + carry) % 10
            dummy.next = ListNode(val=digit)
            
            # increment pointers and update carry
            carry = (p1.val + p2.val + carry) // 10
            dummy = dummy.next
            p1 = p1.next
            p2 = p2.next
          
        # if list 1 has more numbers
        while p1 != None:
            # create new node
            digit = (p1.val + carry) % 10
            dummy.next = ListNode(val=digit)
            
            # increment pointers
            carry = (p1.val + carry) // 10
            dummy = dummy.next
            p1 = p1.next

        # if list2 has more numbers
        while p2 != None:
            # create new node
            digit = (p2.val + carry) % 10
            dummy.next = ListNode(val=digit)
            
            # increment pointers
            carry = (p2.val + carry) // 10
            dummy = dummy.next
            p2 = p2.next
            
        # edge case of leftover '1'
        if carry == 1: dummy.next = ListNode(carry)

        return res.next