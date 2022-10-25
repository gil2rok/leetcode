class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        # return self.naive_sol(nums)
        return self.optimized_sol(nums)
        
    def optimized_sol(self, nums):
        # optimized sol w/ early stopping
        counts = dict()
        
        for i, n in enumerate(nums):
            counts[n] = counts.get(n, 0) + 1
            if counts[n] == 2:
                return n
        
    def naive_sol(self, nums):
        # naive sol
        counts = dict()
        
        for n in nums:
            counts[n] = counts.get(n,0) + 1
            
        n = len(nums) / 2
        for k, v in counts.items():
            if v == n:
                return k