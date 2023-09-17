class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        check = {}
        for num in nums:
            if check.get(num) is None:
                check[num] = True
            else:
                return True
        return False 