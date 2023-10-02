# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []

        def traverse(node, path):
            if node is None:
                return
            if not node.left and not node.right:
                result.append('->'.join(map(str, path + [node.val])))
                return
            traverse(node.left, path + [node.val])
            traverse(node.right, path + [node.val])

        traverse(root, [])
        return result