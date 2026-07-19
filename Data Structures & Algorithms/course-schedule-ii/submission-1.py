from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = { i:[] for i in range(numCourses) }

        inDeg  = [0] * numCourses
        for u,v in prerequisites:
            adj[u].append(v)

            inDeg[v] += 1

        que = deque()
        for i, deg in enumerate(inDeg):
            if deg == 0:
                que.append(i)

        output = []
        while que:
            node = que.popleft()
            output.append(node)
            for it in adj[node]:
                inDeg[it] -= 1
                if inDeg[it] == 0:
                    que.append(it)
        
        output.reverse()
        if len(output) != numCourses: return []
        return output



