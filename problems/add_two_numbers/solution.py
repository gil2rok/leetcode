# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    ##### Time O(m + n) | Space O(1)
    # m = len(l1), n = len(l2)
    # space does not include required output
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        
        cur = dummy
        while l1 or l2 or carry:
            # extract numerical value if not reached end of list
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
    
            # create new node
            digit = (v1 + v2 + carry) % 10
            cur.next = ListNode(digit)
            
            # increment pointers and update carry 
            carry = (v1 + v2 + carry) // 10
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
        
#     ##### Time O(m+n) | Space O(1) #####
#     # m = len(l1), n = len(l2)
#     # space does not include required output
    
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         carry = 0
#         dummy = ListNode()
        
#         # add up numbers in both list1 and list2
#         cur = dummy
#         while l1 != None and l2 != None:
#             # create new node
#             digit = (l1.val + l2.val + carry) % 10
#             cur.next = ListNode(val=digit)
            
#             # increment pointers and update carry
#             carry = (l1.val + l2.val + carry) // 10
#             cur = cur.next
#             l1 = l1.next
#             l2 = l2.next
          
#         # if list 1 has more numbers
#         while l1 != None:
#             # create new node
#             digit = (l1.val + carry) % 10
#             cur.next = ListNode(val=digit)
            
#             # increment pointers
#             carry = (l1.val + carry) // 10
#             cur = cur.next
#             l1 = l1.next

#         # if list2 has more numbers
#         while l2 != None:
#             # create new node
#             digit = (l2.val + carry) % 10
#             cur.next = ListNode(val=digit)
            
#             # increment pointers
#             carry = (l2.val + carry) // 10
#             cur = cur.next
#             l2 = l2.next
            
#         # edge case of leftover '1'
#         if carry == 1: cur.next = ListNode(carry)

#         return dummy.next