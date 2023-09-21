from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        idx_dict = defaultdict(list)
        for i in range(len(s)-1, -1, -1):
            idx_dict[s[i]].append(i)
        check = set()
        start, max_v, cur = 0, 0, 0

        for i in range(len(s)):
            if s[i] in check:
                check = set()
                temp = idx_dict[s[i]].pop()
                while temp < start:
                    temp = idx_dict[s[i]].pop()
                start = temp
                for j in range(start + 1, i + 1):
                    check.add(s[j])
                max_v = max(max_v, cur)
                cur = len(check)
            else:
                cur += 1
                check.add(s[i])
        else:
            max_v = max(max_v, cur)
        return max_v