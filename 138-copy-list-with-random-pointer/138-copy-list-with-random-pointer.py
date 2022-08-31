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
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        ##### Time O(2n) | Space O(n) #####
        copy_head = Node(0) # dummy node
        orig_dict = dict() # original node --> copy node
        
        # copy .next attribute
        cur, copy = head, copy_head
        while cur != None:
            copy.next = Node(cur.val)
            copy = copy.next
            orig_dict[cur] = copy
            cur = cur.next
                    
        # copy .random attribute
        cur, copy = head, copy_head.next
        while cur != None:
            if cur.random == None:
                copy.random = None
            else:
                copy.random = orig_dict[cur.random]
            cur = cur.next
            copy = copy.next
            
        return copy_head.next
        