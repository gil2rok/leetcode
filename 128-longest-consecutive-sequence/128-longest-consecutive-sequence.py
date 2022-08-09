class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0

        consecutive_lengths = dict()
        nums_set = set(nums)
        
        for n in nums:
            if n not in nums_set:
                continue
                
            start = 1
            end = 1
 
            while n - start in nums_set:
                nums_set.remove(n - start)
                start += 1
            while n + end in nums_set:
                nums_set.remove(n + end)
                end += 1
                
            consecutive_lengths[n] = start + end - 1
            nums_set.remove(n)
            
        return max(consecutive_lengths.values())