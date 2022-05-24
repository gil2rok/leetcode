class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        prev = nums[0]
        offset = 0
        
        # loop over all numbers
        # time O(n), space O(1)
        for i, cur in enumerate(nums[1:]):
            # if duplicate
            if cur == prev:
                offset -= 1
            nums[i + 1 + offset] = cur
            prev = cur
        return len(nums) + offset
        '''
        
        # init dict
        no_duplicates = dict()
        
        # insert nums into dict
        # Time O(n), Space O(m) w/ m = hashmap sz
        for num in nums:
            no_duplicates[str(num)] = num
            
        count = 0
        # extract nums from dict
        # Time O(k), Space O(1)
        for i, val in enumerate(no_duplicates.values()):
            nums[i] = val
            count += 1
            
        return count