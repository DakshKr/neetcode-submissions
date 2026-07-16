class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        n = len(text1)
        m = len(text2)

        dp = {}
        def fn(i, j):
            if i == n or j == m:
                return 0

            if (i, j) in dp:
                return dp[(i,j)] 
            
            inc = 1 if text1[i] == text2[j] else 0


            dp[(i,j)] = max( inc + fn(i+1, j+1), 
                        fn(i, j+1),
                        fn(i+1, j))
            return dp[(i,j)]

        return fn(0, 0)