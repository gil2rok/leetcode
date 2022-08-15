class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]: 
        sol = set() # set of sorted tuples
        nums = sorted(nums) # O(nlogn)
        
        for idx, target in enumerate(nums): #O(n)
            l, r = 0, len(nums) - 1
            
            # ensure l and r pointers are not at idx
            if l == idx: l += 1
            if r == idx: r -=1
            
            while l < r:
                threesum = nums[l] + nums[r] + target
                
                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
                elif threesum == 0:
                    sol.add(tuple(sorted([nums[l], nums[r], target])) ) #O(1)
                        
                    # move l and r pointers until reach new, unique val
                    # to avoid adding redundant triples (nums[l], nums[r], target)
                    l_temp, r_temp = nums[l], nums[r]
                    while nums[l] == l_temp and l<r:
                        l += 1
                    while nums[r] == r_temp and l<r:
                        r -= 1
                    
                # ensure l and r pointers are not at idx
                if l == idx: l += 1
                if r == idx: r -=1
        return sol