from collections import defaultdict
from heapq import heappush, heapreplace, heappop

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return self.n_sol(nums, k)
        
    def n_sol(self, nums, k):
        freq = dict()
        for i in nums:
            freq[i] = 1 + freq.get(i, 0)
        
        bucket = [[] for i in range(len(nums) + 1)]
        for num, count in freq.items():
            bucket[count].append(num)
            
        res = []
        for count in range(len(nums), 0, -1):
            print(count)
            for num in bucket[count]:
                res.append(num)
                if len(res) == k:
                    return res
        
    def nlogk_sol(self, nums, k):
        # initialize and fill frequency dict
        freq_dict = defaultdict(lambda: 0)
        for i in nums:
            freq_dict[i] += 1
        
        # find k highest frequencies 
        count = 0
        heap = []
        for key, val in freq_dict.items():
            # fill heap with first k elements
            if count < k:
                heappush(heap, (val,key))
                count += 1
                
            # ensure heap contains k most frequent elements
            else:
                min_heap_freq = heap[0][0]
                if val > min_heap_freq:
                    heapreplace(heap, (val,key))

        # extract elements with k highest frequencies from heap
        res = [None] * k
        for i in range(k):
            val, key = heappop(heap)
            res[i] = key        
        return res
        
            
        