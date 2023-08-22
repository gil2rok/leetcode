class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        dp = [0] * (n + 1)
        m = [[] for _ in range(n)]
        for s, e, g, in offers:
            m[e].append([s, g])
        for e in range(1, n + 1):
            dp[e] = dp[e - 1]
            for s, g in m[e - 1]:
                dp[e] = max(dp[e], dp[s] + g)
        return dp[-1]
