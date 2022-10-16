class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        distinct = set()
        for n in nums:
            reverse_n = int(str(n)[::-1])
            
            distinct.add(n)
            distinct.add(reverse_n)
            
        return len(distinct)
        