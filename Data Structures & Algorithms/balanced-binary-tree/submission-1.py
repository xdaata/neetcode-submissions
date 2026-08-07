# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isBalance = True
        def dfc(root):
            if not root:
                return 0

            left_h = dfc(root.left)
            right_h = dfc(root.right)
            if abs(left_h - right_h) > 1:
                self.isBalance = False

            return 1 + max(left_h, right_h)
        dfc(root)
        return self.isBalance