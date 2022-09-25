class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_val = nums[0]
        max_len = 1
        
        l = 0
        for r in range(1, len(nums)):
            #print(nums[l:r+1], max_val, max_len)
            if nums[r] == nums[l] == max_val:
                max_len = max(max_len, r - l + 1)
            elif nums[r] > max_val:
                max_val = nums[r]
                max_len = 1
                l = r
            else:
                l = r
        return max_len