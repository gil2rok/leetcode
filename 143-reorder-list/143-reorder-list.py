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
        
        loc = dict() # idx in linked list : node
        idx = 0
        pt = head
        
        # add all elements to loc dict
        while pt != None:
            loc[idx] = pt
            pt = pt.next
            idx += 1
        
        # while loc dict is not empty
        l, r, = 0, idx-1
        while l + 1 < r:
            #print(loc[l].next)
            #print(loc[r])
            
            loc[r-1].next = None
            loc[r].next = loc[l+1]
            loc[l].next = loc[r]
            
            l += 1
            r -= 1
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        
        
        
#         # edge case if linked list is empty, contains 1 element, or contains 2 elements
#         # TODO: do I want to check case when head.next.next == None?
#         if head == None or head.next == None or head.next.next == None:
#             return head
    
#         prev = head
#         cur = head.next
        
#         # construct doubely linked-list
#         dll = [] # doublely linked-list
#         dll.append((None, cur))
#         while cur != None:
#             print(dll)
#             dll.append((prev, cur.next))
#             prev = cur
#             cur = cur.next
            
#         for i in range(len(dll) // 2):
#             dll[-i]
            
            
#         Naive Approach O(n^2)
#         pt = head
#         while pt.next.next != None:
#             tail2 = pt
            
#             while tail2.next.next != None:
#                 tail2 = tail2.next
#             tail = tail2.next
#             tail2.next = None
                    
#             tmp = pt.next
#             pt.next = tail
#             tail.next = tmp
#             pt = tmp
#         return head