from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
            m x n matrix
            -1, 0 , inf
        """

        n = len(grid)
        m = len(grid[0])
        vis = set()

        def bfs(x,y):
          
            que = deque()
            que.append((x,y,0))
            change = [(0,1), (0,-1), (1,0), (-1, 0) ]

            while que:
                row, col, dis = que.popleft()

                for ci,cj in change:
                    new_row =  row + ci
                    new_col = col + cj

                    if (new_row in range(n) and
                        new_col in range(m) and
                     
                        grid[new_row][new_col] > grid[row][col]):
                        
                        grid[new_row][new_col] = dis+1
                        que.append((new_row, new_col,dis+1))

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    bfs(i,j)

[2147483647,    -1,         0,          1],
[2147483647,    2147483647, 1,          -1],
[2147483647,     -1,        2147483647,     -1],
[0,                -1,      2147483647, 2147483647]
        
