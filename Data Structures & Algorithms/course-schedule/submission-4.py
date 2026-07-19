class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        status = {}

        for u,v in prerequisites:
            if u in adj:
                adj[u].append(v)
            else:
                adj[u] = [v]

        for i in range(numCourses):
            status[i] = 0
            if i not in adj:
                adj[i] = []

        def checkLoopViaDfs(node):
            if status[node] == 2:
                return False
            
            status[node] = 1
            output = False
            for it in adj[node]:
                if status[it] == 1:
                    return True
                elif status[it] == 2:
                    continue
                else:
                    output = output or checkLoopViaDfs(it)
            status[node] = 2
            
            return output
        
        for n in adj:
            if status[n] == 0 and checkLoopViaDfs(n):
                return False
        return True
