#import copy

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        ######## SOL 1 #########
        # times out
        
        '''
        # Runtime: O(kn)
        for _ in range(k):
            prev = nums[0]
            
            for i, num in enumerate(nums[:-1]):
                temp = nums[i+1]
                nums[i+1] = prev
                prev = temp
                
            nums[0] = prev
        '''
                
        ####### SOL 2 ######
        
        if k == 0:
            return
           
        n = len(nums)
        prev = nums[:k+1]

        for i, num in enumerate(nums):
            new_idx = (i+k) % n
            
            temp = nums[new_idx]
            nums[new_idx] = prev[i % k]
            prev[i % k] = temp
        
        