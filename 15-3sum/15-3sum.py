class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sol = set() # set of sorted tuples
        nums = sorted(nums) # O(nlogn)
        
        for idx, target in enumerate(nums): #O(n)
            l, r = 0, len(nums) - 1
            
            # ensure l and r pointers are not at idx
            #print('IDX:\t', idx, l)
            if l == idx: l += 1
            if r == idx: r -=1
            
            #print(nums, -target)
            while l < r: # O(n)
                #print(nums[l], nums[r], nums[l]+nums[r]+target)
                
                # if sum of three nums == 0 without duplicates, add to sol
                if nums[l] + nums[r] + target == 0:
                    
                    # check candidate sol is not already in solution set
                    candidate_sol = tuple(sorted([nums[l], nums[r], target])) 
                    if candidate_sol not in sol: #O(1)
                        #print('Adding sol:\t', candidate_sol)
                        sol.add(candidate_sol) #O(1)
                        
                    # move l and r pointers until reach new, unique val
                    # to avoid adding redundant triples (nums[l], nums[r], target)
                    l_temp, r_temp = nums[l], nums[r]
                    while nums[l] == l_temp and l<r:
                        l += 1
                    while nums[r] == r_temp and l<r:
                        r -= 1
                    
                # if sum of three nums > 0, decrement right pointer
                elif nums[l] + nums[r] + target > 0:
                    r -=1
                    
                # if sum of three nums < 0, increment left pointer
                elif nums[l] + nums[r] + target < 0:
                    l += 1
                    
                # ensure l and r pointers are not at idx
                #print('IDX:\t', idx, l)
                if l == idx: l += 1
                if r == idx: r -=1
                    
            #print('\n')
        return sol