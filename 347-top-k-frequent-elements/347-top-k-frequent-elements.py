from collections import defaultdict
from heapq import heappush, heapreplace, heappop, nsmallest

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # return self.n_sol(nums, k)
        # return self.klogn_sol(nums, k)
        return self.klogn_sol(nums, k)
        
    def n_sol(self, nums, k):
        # count frequency with dict O(n)
        freq = dict()
        for i in nums:
            freq[i] = 1 + freq.get(i, 0)
        
        # use bucket sort O(n)
        bucket = [[] for i in range(len(nums) + 1)]
        for num, count in freq.items():
            bucket[count].append(num)
            
        # find k most frequent elements O(k)
        res = []
        for count in range(len(nums), 0, -1):
            for num in bucket[count]:
                res.append(num)
                if len(res) == k:
                    return res
    
    def klogn_sol(self, nums, k):
        # count frequency with dict O(n)
        freq = dict()
        for n in nums:
            freq[n] = 1 + freq.get(n, 0)
            
        # insert freq dict into min-heap O(n)
        # negate frequency values b/c really want max-heap
        heap = [(-c, n) for n, c in freq.items()]
        heapify(heap)
        
        # extract k most frequent nums
        res = []
        for _ in range(k):
            (c, n) = heappop(heap)
            res.append(n)
        
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
        
            
        