class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        res = self.my_sum(1, n + 1)
        if k < n * 2: # non k-avoiding array
            start = k // 2 + 1
            stop = min(k, n + 1)            
            res -= 2 * self.my_sum(start, stop)
            res += (n + k) * (stop - start)
        return res
    
    def mimimumSum_old(self, n, k):
        res = [i for i in range(1, n+1)]
        if k < n * 2: # non k-avoiding array
            for i in range(k // 2 + 1, min(k, n + 1)):
                res[i - 1] += n + k - 2 * i
                # res[i - 1] = n + k - i
 
        return sum(res)

    def my_sum(self, start, stop):
        n = stop - start
        return int(n * (n + 1) / 2) + (n * (start - 1))