class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        if x[0] == '-':
            if -int(x[:0:-1]) < -2147483648:
                return 0
            else:
                return -int(x[:0:-1])
        elif int(x[::-1]) > 2147483647:
            return 0
        return int(x[::-1])