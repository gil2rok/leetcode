# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Time O(n) | Space O(1)
        # while head != None:
        #     if head.val > 10e5:
        #         return True
        #     head.val = 10e5 + 1
        #     head = head.next
        # return False
        
        # Time O(n) | Space O(n)
        visited = dict()
        while head != None:
            if head in visited:
                return True
            visited[head] = True
            head = head.next
        return False