class Solution:
    def climbStairs(self, n: int) -> int:
        """

        for every i th place I can go to i+1 or i+2 
        and i need all possible compination

        or i can say to find ways to reach n 
        i need to find no of ways i readed n-1 and n-2 and add them togther         

        """
        """
        dp = [None for _ in range(n+1) ]
        def fn(i):
            if i <= 1 : return 1
            print(i)
            if dp[i] !=  None : return dp[i]

            dp[i] = fn(i-1) + fn(i-2)

            return dp[i]
        return fn(n)
        """
        prev1, prev2 = 2,1
        
        if n == 1: return prev2
        if n == 2: return prev1
        
        for i in range(3, n+1):
            curr = prev1+ prev2
            prev2 = prev1
            prev1 = curr
        return prev1

        