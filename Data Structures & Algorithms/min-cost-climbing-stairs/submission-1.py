class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        dp = [None for _ in range(len(cost) + 1)]
        def fn(i):
            
            if i == 1 or i == 0: return 0
            if dp[i] != None: return dp[i]

            c1 = fn(i-1) + cost[i-1]
            c2 = fn(i-2) + cost[i-2]          
            dp[i] = min(c1, c2)
            return dp[i]

        return fn(len(cost))
        