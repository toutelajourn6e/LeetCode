class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        elif n % 2:
            return False
        
        num = 1
        for i in range(32):
            num <<= 1
            if num == n:
                return True
        return False