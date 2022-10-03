# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    ##### Time O(n) | Space O(1) #####
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        seen_p, seen_q, lca = self.recurse(root, False, False, p, q, None)
        return lca
        
    def recurse(self, node, seen_p, seen_q, p, q, lca):
        # base case
        if node == None:
            return seen_p, seen_q, lca
        
        # recurse
        p_left, q_left, lca_left = self.recurse(node.left, seen_p, seen_q, p, q, lca)
        p_right, q_right, lca_right = self.recurse(node.right, seen_p, seen_q, p, q, lca)
        
        # ensure don't override lca
        if lca_left != None:
            return p_left, q_left, lca_left
        if lca_right != None:
            return p_right, q_right, lca_right
        
        seen_p = p_left or p_right or (node == p)
        seen_q = q_left or q_right or (node == q)
        
        # check if root is lowest common ancestor
        if seen_p and seen_q:
            lca = node
        
        return seen_p, seen_q, lca