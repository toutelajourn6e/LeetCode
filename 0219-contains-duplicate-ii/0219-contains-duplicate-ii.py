class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        check = {}
        for i in range(len(nums)):
            if check.get(nums[i]) is None:
                check[nums[i]] = i
            else:
                if abs(check[nums[i]] - i) <= k:
                    return True
                else:
                    check[nums[i]] = i
        return False