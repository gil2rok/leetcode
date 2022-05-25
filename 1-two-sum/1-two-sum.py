class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ##### SOL 1 #####
        # O(n^2)
        # target = n1 + n2
        
        for i, n1 in enumerate(nums):
            n2 = target - n1
            
            for j, num in enumerate(nums[i+1:]):
                if n2 == num:
                    return [i, j + i + 1]
        