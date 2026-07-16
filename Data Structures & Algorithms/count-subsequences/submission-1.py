class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)

        dp = {}
        def fn(i , j):
            if j == m:
                return 1
            if i == n:
                return 0

            if (i,j) in dp:
                return dp[(i,j)]

            if s[i] == t[j]:

                dp[(i,j)] =  fn(i+1, j+1) + fn(i+1,j)
                return dp[(i,j)]

            dp[(i,j)] = fn(i+1, j)
            return dp[(i,j)] 
        
        return fn(0,0)