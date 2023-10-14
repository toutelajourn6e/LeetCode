# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ans = []
        def inorder(node):
            if node is None: return
            elif node.left and node.left.left is None and node.left.right is None:
                ans.append(node.left.val)
            
            inorder(node.left)
            inorder(node.right)
        inorder(root)
        return sum(ans)