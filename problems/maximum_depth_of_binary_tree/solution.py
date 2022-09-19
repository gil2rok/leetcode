# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.helper(root, 0)
    
    def helper(self, root, level):
        # base case
        if root == None:
            return level
        
        l_height = self.helper(root.left, level+1)
        r_height = self.helper(root.right, level+1)
        
        return max(l_height, r_height)