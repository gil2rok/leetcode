class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l, r = 0, 1
        max_profit = 0
        
        while r < len(prices):
            
            #print(prices[l], prices[r], '\t\t', max_profit)
            if prices[l] > prices[r]:
                l += 1
            elif prices[l] <= prices[r]:
                max_profit = max(max_profit, prices[r] - prices[l])
                r += 1
                
        return max_profit