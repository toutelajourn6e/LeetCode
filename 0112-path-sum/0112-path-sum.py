# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None: return False

        def dfs(node, total):
            if node is None: return 0
            total += node.val
            if node.left is None and node.right is None:
                if total == targetSum: return 1
                else: return 0
            
            return dfs(node.left, total) + dfs(node.right, total)

        return True if dfs(root, 0) else False

            
