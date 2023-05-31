# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import math
from heapq import heappush, heappop, heappushpop
from collections import deque

class Solution:
    # Time: O(k) | Space: O(k)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # in-order traversal via DFS and implemented with recursion
        stack = []
        cur = root

        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            k -= 1
            if k == 0: return cur.val
            cur = cur.right
