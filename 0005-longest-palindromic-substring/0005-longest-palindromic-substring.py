class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_leng = 0
        ans = s[0]

        for i in range(len(s)):
            leng = 0
            left, right = i, i+1
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    leng += 2
                    left -= 1
                    right += 1
                else: break
            if leng > max_leng:
                max_leng = leng
                ans = s[left+1:right]
            if i > 0 and i < len(s)-1:
                leng = 1
                left, right = i - 1, i + 1
                while left >= 0 and right < len(s):
                    if s[left] == s[right]:
                        leng += 2
                        left -= 1
                        right += 1
                    else: break
            if leng > max_leng:
                max_leng = leng
                ans = s[left+1:right]
        return ans