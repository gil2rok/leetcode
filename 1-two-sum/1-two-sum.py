class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ##### SOL 1 #####
        # O(n^2) naive search
        
        '''
        for i, n1 in enumerate(nums):
            n2 = target - n1
            
            for j, num in enumerate(nums[i+1:]):
                if n2 == num:
                    return [i, j + i + 1]
        '''
        
        ##### SOL 2 #####
        # O(nlogn) sort then use two pointers
        
        '''
        # check edge case
        if target % 2 == 0: # if target is even
            count = 0
            idx_list = []
            for i, num in enumerate(nums):
                if num == target / 2:
                    count += 1
                    idx_list.append(i)
            if count == 2:
                return idx_list
                    
        
        # create dict to store original idicies 
        idx_dict = dict()
        for i, num in enumerate(nums):
            idx_dict[num] = i
        
        nums = sorted(nums)
        p1 = 0; p2 = len(nums) - 1
        
        # modify two pointers
        while p1 < p2:
            attempt = nums[p1] + nums[p2]
            error = target - attempt
            
            if error == 0:
                idx1 = idx_dict[nums[p1]]
                idx2 = idx_dict[nums[p2]]
                return [idx1, idx2]
            elif error > 0:
                p1 += 1
            elif error < 0:
                p2 -= 1
        '''
        
        ##### SOL 3 #####
        # O(n)
        
        prev = {} # {num: idx}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prev:
                return [prev[diff], i]
            prev[n] = i