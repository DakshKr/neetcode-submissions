class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        n = len(prices)
        bought = False

        for i in range(n-1):
            if prices[i] > prices[i+1] and bought:
                profit += prices[i]
                bought = False
            
            elif prices[i] <= prices[i+1] and not bought:
                profit -= prices[i]
                bought = True
        
        if bought:
            profit += prices[-1]
        
        return profit


        #  7 1 5 3 6 4
        #  b = F    ,       
            