class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [None for _ in range( len(s) + 1  )]
        def fn(i):
            if i >= n: return 1
            if int(s[i]) <= 0: return 0
            if i == n-1: return 1


            if dp[i] != None:
                return dp[i]

            output = fn(i+1)
            if int(s[i: i+2]) < 27:
                output += fn(i+2)
            
            dp[i] = output
            return dp[i]
 
        return fn(0)
