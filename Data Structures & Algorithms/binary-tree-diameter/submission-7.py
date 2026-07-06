# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.output = 0
        def fn(node):
            if not node: return 0

            max_height = fn(node.left)
            max_height2 = fn(node.right)

            self.output = max( max_height + max_height2 , self.output )
            return 1 + max(max_height, max_height2)

        fn(root)
        return self.output




