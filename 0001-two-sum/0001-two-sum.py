class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_nums = {}

        for i in range(len(nums)):
            key = target - nums[i]
            if dict_nums.get(key) is not None:
                return [i, dict_nums[key]]
            dict_nums[nums[i]] = i