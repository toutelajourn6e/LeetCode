class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s: return True
        idx = 0
        for ch in t:
            if ch == s[idx]:
                idx += 1
            if idx == len(s): return True
        return False