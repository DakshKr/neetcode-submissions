from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        n = len(heights)
        m = len(heights[0])

        pacific_list = set()
    
        que = deque()
        for i in range(m):
            que.append((0, i))
            pacific_list.add((0, i))
        for i in range(1,n):
            que.append((i,0))
            pacific_list.add((i,0))
        change  = [ (0,1), (0,-1), (1,0), (-1,0)  ]
        while que:
            row, col = que.popleft()

            for cr, cc in change:
                new_row = row + cr
                new_col = col + cc

                if (new_row in range(n) and
                    new_col in range(m) and
                    (new_row,new_col) not in pacific_list and
                    heights[new_row][new_col] >= heights[row][col] ):

                    pacific_list.add((new_row,new_col))
                    que.append((new_row,new_col))
        
        atlantic_list = set()
        que = deque()
        for i in range(m):
            que.append((n-1, i))
            atlantic_list.add((n-1, i))
        for i in range(0,n-1):
            que.append((i,m-1))
            atlantic_list.add((i,m-1))
        while que:
            row, col = que.popleft()

            for cr, cc in change:
                new_row = row + cr
                new_col = col + cc

                if (new_row in range(n) and
                    new_col in range(m) and
                    (new_row,new_col) not in atlantic_list and
                    heights[new_row][new_col] >= heights[row][col] ):

                    atlantic_list.add((new_row,new_col))
                    que.append((new_row,new_col))
                      

        return list(atlantic_list.intersection(pacific_list))
        

