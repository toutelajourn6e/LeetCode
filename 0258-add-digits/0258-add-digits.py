class Solution:
    def addDigits(self, num: int) -> int:
        digit = list(str(num))
        while len(digit) > 1:
            num = sum(map(int, digit))
            digit = list(str(num))
        return int(digit[0])