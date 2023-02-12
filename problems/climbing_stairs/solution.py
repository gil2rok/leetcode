class Solution:
    def climbStairs(self, n: int) -> int:
        t1, t2 = 1, 1

        for i in range(n - 1):
            tmp = t1
            t1 = t2 + t1
            t2 = tmp

        return t1