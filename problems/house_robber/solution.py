class Solution:
    ##### Time O(n) | Space O(n) #####
    def rob(self, nums: List[int]) -> int:
        # edge cases
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        # init dp array
        dp = [-1] * len(nums)
        
        # setup intial dp values
        dp[len(nums)-1] = nums[-1]
        dp[len(nums) - 2] = max(nums[-1], nums[-2])
        
        # iterate through dp recurrence
        for i in range(len(nums)-3, -1, -1): 
            dp[i] = max(nums[i] + dp[i+2], dp[i+1])
            
        return dp[0]
            
        