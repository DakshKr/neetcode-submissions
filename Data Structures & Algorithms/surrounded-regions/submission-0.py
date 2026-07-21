from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        que = deque()
        vis = set()
        n = len(board)
        m = len(board[0])

        for i in range(m):
            if board[0][i] == "O":
                que.append( (0,i) )
                vis.add( (0,i) )

            if n > 1 and board[n-1][i] == "O":
                que.append( (n-1,i) )
                vis.add( (n-1,i) )

        for j in range(1,n-1):
            if board[j][0] == "O":
                que.append( (j,0) )
                vis.add( (j,0) )
            
            if m > 1 and board[j][m-1] == "O":
                que.append( (j,m-1) )
                vis.add( (j, m-1) )
        
        change = [ (0,1), (0,-1), (1,0), (-1, 0) ]
        while que:
            r,c = que.popleft()

            for cr, cc in change:
                new_r = r + cr
                new_c = c + cc

                if (new_r in range(n) and
                    new_c in range(m) and
                    board[new_r][new_c] == "O" and
                    (new_r, new_c) not in vis):

                    que.append( (new_r, new_c) )
                    vis.add( (new_r, new_c))
        
        for i in range(n):
            for j in range(m):
                if (i,j) not in vis:
                    board[i][j] = "X"




