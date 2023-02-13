class Solution:
    def rob(self, nums: List[int]) -> int: 
        if len(nums) == 1:
            return nums[0]
            
        return max(self.helper(nums[:-1]), self.helper(nums[1:]))

    def helper(self, nums):
        t1, t2 = 0, 0
        for n in nums:
            tmp = max(t1 + n, t2)
            t1 = t2
            t2 = tmp
        return t2