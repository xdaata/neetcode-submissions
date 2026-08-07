# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        pre_idx = 0

        def make(left_bound, right_bound):
            nonlocal pre_idx

            if left_bound > right_bound:
                return None

            root_val = preorder[pre_idx]
            root = TreeNode(root_val)
            pre_idx += 1

            mid_idx = inorder_map[root_val]

            root.left = make(left_bound, mid_idx - 1)
            root.right = make(mid_idx + 1, right_bound)

            return root
        
        return make(0, len(preorder) - 1)
        