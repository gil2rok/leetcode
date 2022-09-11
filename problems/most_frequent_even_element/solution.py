class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        max_even = -1
        counts = dict()
        counts[max_even] = 0
        
        for n in nums:
            if n % 2 == 0:
                counts[n] = 1 + counts.get(n, 0)
                
                if counts[n] > counts[max_even]:
                    max_even = n     
                elif counts[n] == counts[max_even]:
                    max_even = min(n, max_even)
        return max_even
                
            