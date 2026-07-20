from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #store are the original rotten oranages in some data structure
        n = len(grid)
        m = len(grid[0])    


        matrix = [[float("inf")] * m for _ in range(n) ]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    matrix[i][j] = 0
                elif grid[i][j] == 0:
                    matrix[i][j] = -1


        def bfs(r,c):
            
            que = deque()
            que.append((r,c, 0))
            change = [ (0,1),(0,-1),(1,0),(-1,0) ]

            while que:
                row, col, _min = que.popleft()

            
                for cr, cc in change:
                    new_row = row + cr
                    new_col = col + cc

                    if (new_row in range(n) and
                        new_col in range(m) and
                        grid[new_row][new_col] == 1 and
                        matrix[new_row][new_col] > _min):
                        
                        que.append((new_row, new_col, _min + 1))
                        matrix[new_row][new_col] = _min + 1


        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    bfs(i,j)
        
      
        _max = 0
        for arr in matrix:
            _max = max(max(arr), _max)
        
        if _max == float("inf"): 
            return -1
        else:
            return _max





"""
2   1   0   1
0   1   1   1
0   1   2   1

empty = -1
rotten = 0
inf

0    1   -1  3  
-1   2   1   2  
-1   1   0   1 

"""