"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        
        newNode = Node(node.val)
        que = deque()
        que.append((node, newNode))
        vis = {}
           
        while que:
            
            old_node, new_node = que.popleft()


            for it in old_node.neighbors:
                if it not in vis:

                    new_it = Node(it.val)
                    new_node.neighbors.append(new_it)

                    vis[it] = new_it
                    que.append((it, new_it)) 
                else:
                    new_node.neighbors.append(vis[it])

        return newNode