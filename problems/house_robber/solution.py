class Solution:
    def rob(self, nums: List[int]) -> int:
        # edge case
        if len(nums) == 1:
            return nums[0]

        t2, t1 = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            tmp = t1
            t1 = max(nums[i] + t2, t1)
            t2 = tmp

        return t1