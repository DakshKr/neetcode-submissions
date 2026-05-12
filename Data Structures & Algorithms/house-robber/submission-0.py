class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        dp = [ None for _ in range(n) ]
        
        def fn(i):
            if i == 0: 
                return nums[0]
            if i == -1: 
                return 0

            if dp[i] != None: return dp[i]
            
            c1 = fn(i-1)
            c2 = fn(i-2) + nums[i]
            
            dp[i] = max(c1, c2)
            return dp[i]

        return fn( n-1 )