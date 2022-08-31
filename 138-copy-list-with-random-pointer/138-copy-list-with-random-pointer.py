"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
from heapq import heappush, heappop

class Solution:
    ##### Time O(2n) | Space O(n) #####
    # space excludes the deep copy itself
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]': 
        oldToCopy = {None : None} # old node --> deep copy of old node
        
        # fill dict with old and copy nodes
        cur = head
        while cur != None:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next
        
        cur = head
        while cur != None:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next
        return oldToCopy[head]
            
        
#     ##### Time O(2n) | Space O(n) #####
#     # space excludes the deep copy itself
#     def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]': 
#         copy_head = Node(0) # dummy node
#         orig_dict = dict() # original node --> copy node
        
#         # copy .next attribute
#         cur, copy = head, copy_head
#         while cur != None:
#             copy.next = Node(cur.val)
#             copy = copy.next
#             orig_dict[cur] = copy
#             cur = cur.next
                    
#         # copy .random attribute
#         cur, copy = head, copy_head.next
#         while cur != None:
#             if cur.random == None:
#                 copy.random = None
#             else:
#                 copy.random = orig_dict[cur.random]
#             cur = cur.next
#             copy = copy.next
            
#         return copy_head.next