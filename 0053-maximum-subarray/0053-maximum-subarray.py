class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cursum, maxsum = 0, nums[0]
        for i in range(len(nums)):
            cursum = max(cursum + nums[i], nums[i])
            maxsum = max(maxsum, cursum)
        return maxsum