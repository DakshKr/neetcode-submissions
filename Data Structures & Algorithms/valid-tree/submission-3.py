class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # if there is a loop then not valid
        adj = {i: [] for i in range(n)}
        for u, v in edges:
            adj[v].append(u)
            adj[u].append(v)

        vis = set()

        def isLoop(node, par):
            if node in vis:
                return True

            vis.add(node)

            for it in adj[node]:
                if it != par and isLoop(it, node):
                    return True
            
            return False
        
        if isLoop(0, -1) or len(vis) != n:
            return False
        return True