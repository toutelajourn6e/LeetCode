# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.get_h(root) >= 0

    def get_h(self, node):
        if node is None: return 0
        left, right = self.get_h(node.left), self.get_h(node.right)
        if left < 0 or right < 0 or abs(left - right) > 1: return -1
        return max(left, right) + 1

        