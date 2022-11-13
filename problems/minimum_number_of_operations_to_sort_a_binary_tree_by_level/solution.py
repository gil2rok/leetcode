# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        count_swap = 0
        
        queue = collections.deque()
        queue.append(root)
        
        while queue:
            cur_size = len(queue)
            cur_list = []
            
            while cur_size > 0:
                cur_node = queue.popleft()
                cur_list.append(cur_node.val)
                cur_size -= 1
                
                if cur_node.left != None: queue.append(cur_node.left)
                if cur_node.right != None: queue.append(cur_node.right)
            
            new_idx = self.sanitize_input(cur_list)
            count_swap += self.min_swap(new_idx)
        return count_swap
            
    def sanitize_input(self, nums):
        sort_idx = dict()
        for i, n in enumerate(sorted(nums)):
            sort_idx[n] = i
            
        new_idx = []
        for n in nums:
            new_idx.append(sort_idx[n])
        return new_idx
    
    def min_swap(self, nums):
        # edge case
        if len(nums) == 1: return 0
        
        # init variables
        swap_count = 0
        visited = [False] * len(nums)
        
        # init dict
        idx_to_num = dict() # index i --> nums[i]
        for i, n in enumerate(nums):
            idx_to_num[i] = n
        
        # iterate over all nums
        for i in range(len(nums)):
            if visited[i] == False: # mark unvisited numbers as visited
                visited[i] = True

                if idx_to_num[i] == i: # if num and index are the same
                    continue

                else: # if num and index are different
                    c = idx_to_num[i] # next node
                    
                    while not visited[c]:
                        visited[c] = True
                        c = idx_to_num[c] # next node
                        swap_count += 1
        return swap_count
                
        