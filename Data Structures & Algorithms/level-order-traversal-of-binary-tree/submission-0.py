# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []
        if not root: return output
        
        dq = deque([root])
        while dq:
            l1 = []
            
            while dq:
                l1.append(dq.popleft())

            print(l1)
            output.append([j.val for j in l1])
            for i in l1:
                if i.left:
                    dq.append(i.left)
                if i.right:
                    dq.append(i.right)

        return output

            
