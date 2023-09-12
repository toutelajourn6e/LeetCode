import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        regex = re.compile('[^a-z0-9]')
        s = re.sub(regex, '', s)
        
        if not s or len(s) == 1:
            return True
        else:
            n = len(s) // 2
            for i in range(n):
                if s[i] != s[-1-i]:
                    return False
        return True
        