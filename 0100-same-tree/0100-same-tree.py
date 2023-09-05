# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def check(p_node, q_node):
            if p_node is None and q_node is None:
                return True
            elif p_node is None or q_node is None:
                return False
            elif p_node.val != q_node.val:
                return False
            
            if not check(p_node.left, q_node.left) or not check(p_node.right, q_node.right):
                return False
            else: return True

        return check(p, q)