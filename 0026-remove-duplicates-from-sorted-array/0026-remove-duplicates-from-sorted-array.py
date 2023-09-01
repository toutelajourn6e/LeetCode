class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        compare = -101
        k = 0

        for num in nums:
            if num != compare:
                compare = nums[k] = num
                k += 1
        
        nums = nums[:k]
        return k