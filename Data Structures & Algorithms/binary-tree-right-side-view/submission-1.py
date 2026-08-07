# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res

        q = deque([root])
        while q:
            lvl_size = len(q)
            for i in range(lvl_size):
                curr = q.popleft()

                if i == lvl_size - 1:
                    res.append(curr.val)

                if curr.left: q.append(curr.left)
                if curr.right: q.append(curr.right)

        return res