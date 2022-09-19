# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # base case
        if p == q == None: return True
        if p == None or q == None: return False
        
        # recurse on left and right nodes
        l_same = self.isSameTree(p.left, q.left)
        r_same = self.isSameTree(p.right, q.right)
        
        # combine results
        return l_same and r_same and (p.val == q.val)