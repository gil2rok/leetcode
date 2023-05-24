# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import math
from heapq import heappush, heappop, heappushpop

class Solution:
    # Time: O(n*log(k)) | Space: O(k)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        smallest, counter = [], 0
        largest_k = root.val

        q = collections.deque([root])
        while q: # while have not traversed entire BST
            node = q.popleft() # extract current node
            if not node: continue # skip null node
            
            if counter < k: # when do NOT have k smallest elements
                heappush(smallest, -node.val) # O(log(k))
                largest_k = max(largest_k, node.val)
                counter += 1

            else: # when do have k smallest elements
                if node.val < largest_k: # if found new smaller element
                    heappushpop(smallest, -node.val) # O(log(k))
                    largest_k = smallest[0] * -1

            q.append(node.left)
            q.append(node.right)
        return largest_k