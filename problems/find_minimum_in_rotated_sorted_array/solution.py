class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) <= 3: return min(nums)
        
        l, r = 0, len(nums) - 1
    
        while l<= r:
            if l == r:
                return nums[l]
            
            mid = (l+r) // 2
            #print(nums[l:r+1], '\t', nums[mid], l, r)
            
            # if left subarray properly sorted
            if nums[l] <= nums[mid]:
                if nums[l] < nums[r]:
                    return nums[l]
                else:
                    l = mid + 1
                    
            # if right subarray properly sorted
            else:
                if nums[mid] < nums[mid-1]:
                    return nums[mid]
                else:
                    r = mid - 1