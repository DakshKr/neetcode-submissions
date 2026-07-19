from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # try and make a adj list for ease of use
        adj = {}
        n = len(grid)
        m = len(grid[0])

        change = [(0,1), (1,0), (0,-1), (-1,0)]
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "0": 
                    continue
                

                node = (m*i) + j
                adj[node] = []

                for ci, cj in change:
                    newi = i + ci
                    newj = j + cj

                    if -1<newi < n and -1<newj < m and grid[newi][newj] == "1":
                        new_node = (newi * m) + newj
                                            
                        adj[node].append(new_node)

        output = 0
        vis = set()


        for s in adj:
            if s in vis:
                continue

            print(vis, s)
            output += 1

            vis.add(s)
            que = deque()
            que.append(s)

            while que:
                node = que.popleft()

                for it in adj[node]:
                    if it in vis:
                        continue
                    vis.add(it)
                    que.append(it)
        
        return output
        

        # find number of connected components