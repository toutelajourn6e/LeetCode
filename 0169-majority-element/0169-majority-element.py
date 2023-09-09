from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        max_v, ans = 0, 0

        for key in cnt:
            if max_v < cnt[key]:
                max_v = cnt[key]
                ans = key

        return ans