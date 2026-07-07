# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.output = True
        def isValid(node, _min, _max):
            if self.output == False or not node: 
                return

            if node.val <= _min or node.val >= _max:
                self.output = False
                return
            
            isValid(node.left, _min,  min(_max, node.val))
            isValid(node.right, max(_min, node.val),_max )

        isValid(root, float("-inf"), float("inf"))
        return self.output



