# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res

        q = deque([root])
        while q:
            lvl_size = len(q)
            curr_lvl = []

            for _ in range(lvl_size):
                curr = q.popleft()
                curr_lvl.append(curr.val)

                if curr.left: q.append(curr.left)
                if curr.right: q.append(curr.right)

            res.append(curr_lvl)

        return res