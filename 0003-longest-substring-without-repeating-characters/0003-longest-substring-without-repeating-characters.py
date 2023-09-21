class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check = set()
        max_v, left = 0, 0

        for right in range(len(s)):
            if s[right] not in check:
                check.add(s[right])
                max_v = max(max_v, right - left + 1)
            else:
                while s[right] in check:
                    check.discard(s[left])
                    left += 1
                check.add(s[right])
        return max_v