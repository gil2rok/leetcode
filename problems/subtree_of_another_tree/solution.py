# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time O(S*T) | Space O(1)
    # S = num nodes in root
    # T = num nodes in subRoot
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot == None: return True
        if root == None: return False
        
        if self.sameTree(root, subRoot):
            return True
        
        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))
        
    def sameTree(self, s, t):
        # base case
        if s == None and t == None: return True
        if s == None or t == None: return False
        
        return (self.sameTree(s.left, t.left) and 
                self.sameTree(s.right, t.right) and 
                (s.val == t.val))
            
    
    
#     ##### Time O(n^2) | Space O(1) #####
#     def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
#         # base case
#         if root == None and subRoot == None:
#             return True
#         if root == None or subRoot == None:
#             return False
            
#         # recurse on left and right
#         subtree_in_left = self.isSubtree(root.left, subRoot)
#         subtree_in_right = self.Subtree(root.right, subRoot)
        
#         # combine 
#         if root.val == subRoot.val:
#             subtree_at_root = self.check_subtree(root, subRoot)
#         else:
#             subtree_at_root = False
            
#         return subtree_in_left or subtree_in_right or subtree_at_root
        
#     def check_subtree(self, root, subRoot):
#         # base case
#         if root == subRoot == None: return True
#         if root == None or subRoot == None: return False
        
#         l_subtree = self.check_subtree(root.left, subRoot.left)
#         r_subtree = self.check_subtree(root.right, subRoot.right)
        
#         return l_subtree and r_subtree and (root.val == subRoot.val)
            
        
            
            
            