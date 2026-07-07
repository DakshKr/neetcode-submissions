# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []

        output = [root.val]
        dq = deque([root])

        while dq:
            dqLen = len(dq)
    
            view = None
            for _ in range(dqLen):
                node = dq.popleft()

                if node:
                    dq.append(node.left)
                    dq.append(node.right)

                    if node.right:
                        view = node.right.val
                    elif node.left:
                        view = node.left.val
            
            if view:
                output.append(view)

        return output


                
