class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for i in range(len(nums)):
            if nums[i] == 0:
                next = i
                while nums[next] == 0 and next < len(nums) - 1:
                    next += 1
                nums[i], nums[next] = nums[next], nums[i]
