class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        mask = 0
        for num in nums:
            if mask & (1 << num):
                return num
            mask |= 1 << num