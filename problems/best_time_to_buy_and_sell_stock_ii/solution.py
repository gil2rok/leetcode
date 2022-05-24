class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        profit = 0
        
        # loop over pairs of prices
        for p1, p2 in zip(prices[:-1], prices[1:]):
            diff = p2 - p1
            
            # if trade is profitable
            if diff > 0:
                profit += diff
        return profit
        '''
        
        profit = 0
        p1 = prices[0]
        
        # loop over prices
        for p2 in prices[1:]:
            diff = p2 - p1
            
            # check profitability
            if diff > 0:
                profit += diff
            p1 = p2
            
        return profit