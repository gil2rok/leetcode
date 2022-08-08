import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)
        
        # compute prefix
        for i in range(1, len(nums)):
            answer[i] = answer[i-1] * nums[i-1]
                        
        # compute postfix
        post = 1
        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= post
            post *= nums[i]
            
        return answer
            
        