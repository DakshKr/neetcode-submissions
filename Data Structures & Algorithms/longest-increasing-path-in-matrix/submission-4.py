import sys
sys.setrecursionlimit(10**5) # Set limit to 100,000
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        _max = 0
        n = len(matrix)
        m = len(matrix[0])
        l1 = [[0,1], [0,-1], [1,0], [-1,0]]

        dp = {}
        def fn(i,j):

            if (i,j) in dp:
                return dp[(i,j)]

            output = 1
            for change in l1:
                    i_new = i + change[0]
                    j_new = j + change[1]

                    if -1<i_new < n and -1<j_new < m and matrix[i_new][j_new] > matrix[i][j]:
                        output = max(output, 1 + fn(i_new, j_new))
            
            dp[(i,j)] = output
            return output

        for i in range(n):
            for j in range(m):
                if (i,j) in dp:
                    continue

                _max = max(_max, fn(i,j))

        return _max