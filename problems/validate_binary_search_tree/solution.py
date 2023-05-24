# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import math
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid(node, left, right):
            if node == None: return True # base case

            if not (node.val > left and node.val < right):
                return False


            return (valid(node.left, left, node.val) 
                and valid(node.right, node.val, right)
            )
        
        return valid(root, -math.inf, math.inf)