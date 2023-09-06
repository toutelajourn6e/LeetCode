from string import ascii_uppercase

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        chars = list(ascii_uppercase)
        result = []
        
        while columnNumber:
            columnNumber, digit = divmod(columnNumber - 1, 26)
            digit = chars[digit]
            result.append(digit)
        return ''.join(result[::-1])