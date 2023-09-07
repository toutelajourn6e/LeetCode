# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def BST(start, end):
            if start >= end: return
            mid = (start + end) // 2
            return TreeNode(nums[mid], BST(start, mid), BST(mid + 1, end))
        return BST(0, len(nums))
