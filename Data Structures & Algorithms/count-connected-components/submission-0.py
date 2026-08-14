from collections import deque

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = { i: [] for i in range(n) }
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        comp = 0
        vis = set()

        def dfs(node):
            if node in vis:
                return
            vis.add(node)
            for it in adj[node]:
                dfs(it)

        for NODE in range(n):
            if NODE in vis:
                continue
            comp += 1 
            dfs(NODE)       

        return comp