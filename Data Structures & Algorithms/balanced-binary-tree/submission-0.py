# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        self.status = True
        def checkBalanced(node):
            if not node: return 0

            left = 1 + checkBalanced(node.left)
            right = 1 + checkBalanced(node.right)


            if abs(left - right) > 1:
                self.status = False
            
            return max(right, left)
        
        checkBalanced(root)
        return self.status


