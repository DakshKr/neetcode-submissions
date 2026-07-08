class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = {}

        def fn(amt):
            if amt == 0:
                return 0
            
            
            if amt in dp:
                return dp[amt]

            output = float("inf")

            for coin in coins:
                if coin <= amt:
                    output =  min(output, 1 + fn(amt-coin))
            
            dp[amt] = output
            return output
        
        ans =  fn(amount)
        if ans == float("inf"): return -1
        return ans


            