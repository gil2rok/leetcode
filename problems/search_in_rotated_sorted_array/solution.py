class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (r + l) // 2
            if nums[mid] == target:
                return mid
            
            # if left subarray sorted
            if nums[l] <= nums[mid]:
                # easily check if target is in left subarray
                if nums[l] <= target and target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else: # if right subarray sorted
                # easily check if target is in right subarray
                if target >= nums[mid] and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1