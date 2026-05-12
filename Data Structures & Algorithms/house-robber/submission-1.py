class Solution:
    def rob(self, nums: List[int]) -> int:

        """
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
        """

        n = len(nums)
    
        if n == 1: return nums[0]

        prev2 = nums[0]
        prev1 = max( prev2 , nums[1] )

        for index in range(2, n):
            curr = max( prev1 , prev2 + nums[index])
            prev2 = prev1
            prev1 = curr
            

        return prev1


