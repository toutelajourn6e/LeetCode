# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        ans = 100000

        def dfs(node, depth):
            nonlocal ans
            if node is None: return
            if node.left is None and node.right is None:
                ans = min(depth, ans)
                return

            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 1)
        return ans