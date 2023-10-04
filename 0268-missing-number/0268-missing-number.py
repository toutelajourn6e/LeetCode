class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = (len(nums) * (len(nums) + 1)) // 2
        return n - sum(nums)