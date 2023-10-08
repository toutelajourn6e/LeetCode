class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        start = 1
        while start <= n:
            if start == n: return True
            start *= 3
        return False