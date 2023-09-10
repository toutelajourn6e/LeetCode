class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        for idx, ch in enumerate(columnTitle[::-1]):
            ans += (26 ** idx) * (ord(ch) - 64)
        return ans
