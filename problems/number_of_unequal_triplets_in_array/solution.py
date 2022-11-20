class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        res = 0
        for i, n1 in enumerate(nums):
            for j, n2 in enumerate(nums[i+1:]):
                for n3 in nums[j+i+1:]:
                    
                    if n1 != n2 and n2 != n3 and n3 != n1:
                        res += 1
                    #print(n1, n2, n3, '\t', res)
        return res