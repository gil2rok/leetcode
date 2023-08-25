import heapq
from collections import Counter
class Solution:
    """
    n = len(s)  k = len(set(s))
    Time:   O( nlog(k) )
    Space:  O( n )
    """
    def reorganizeString(self, s: str) -> str:
        heap = [(-v, k) for k, v in Counter(s).items()]
        heapq.heapify(heap)

        prev_a, prev_b = heapq.heappop(heap)
        res = prev_b
        prev_a += 1

        while heap:
            cur_a, cur_b = heapq.heappop(heap)
            res += cur_b
            cur_a += 1

            if prev_a < 0:
                heapq.heappush(heap, (prev_a, prev_b)) # O(logk)
            prev_a, prev_b = cur_a, cur_b

        return res if prev_a == 0 else ""