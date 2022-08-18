class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        l, r = 0, 1 # left = buy, right = sale
        
        for r in range(len(prices)):
            if prices[l] < prices[r]: # if profitable
                max_profit = max(max_profit, prices[r] - prices[l])
            else:
                l = r     
        return max_profit