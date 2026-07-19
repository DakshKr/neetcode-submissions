from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        output = 0
        vis = set()

        def bfs(r,c):
            change = [ (0,1), (0,-1), (1,0), (-1,0) ]
            que = deque()
            que.append( (r,c) )
            vis.add((r,c))

            area = 0

            while que:
                r,c = que.popleft()
                area += 1

                for cr, cc in change:
                    nr = r + cr
                    nc = c + cc

                    if  (nr in range(row) and
                        nc in range(col) and
                        (nr, nc) not in vis and
                        grid[nr][nc] == 1):
                            vis.add((nr, nc))
                            que.append((nr, nc))
            return area

        for r in range(row):
            for c in range(col):
                if (r,c) in vis or grid[r][c] == 0:
                    continue
                
                output = max(output, bfs(r,c))
                
        return output
