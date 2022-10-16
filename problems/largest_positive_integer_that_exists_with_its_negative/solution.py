class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        res = -1
        pos_neg = dict()
        
        for n in nums:
            pos_neg[n] = 1
            
        for n in nums:
            if n > 0 and -n in pos_neg:
                res = max(res, n)
        return res