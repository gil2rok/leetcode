class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = 0 # maximum consecutive length
        nums_set = set(nums)
        
        for n in nums:
            if n not in nums_set:
                continue
                
            start = 1; end = 1
            while n - start in nums_set:
                nums_set.remove(n - start)
                start += 1
            while n + end in nums_set:
                nums_set.remove(n + end)
                end += 1
            nums_set.remove(n)
                
            cur_length = start + end - 1
            max_length = max(cur_length, max_length)
            
        return max_length