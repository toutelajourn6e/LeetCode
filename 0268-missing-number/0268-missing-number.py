class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_set = set([i for i in range(len(nums)+1)])
        for num in nums:
            num_set.discard(num)
        return list(num_set)[0]