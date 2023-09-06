from string import ascii_uppercase

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        chars = [0] + list(ascii_uppercase)
        result = []
        
        while columnNumber:
            columnNumber, digit = divmod(columnNumber, 26)
            print(columnNumber, digit)
            if not digit:
                result.append('Z')
                columnNumber -= 1
            else:   
                digit = chars[digit]
                result.append(digit)
        return ''.join(result[::-1])