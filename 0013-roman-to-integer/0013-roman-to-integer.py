class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        roman_dict = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900, 'I': 1, 'V': 5, 'X': 10,
                    'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for i in roman_dict.keys():
            while i in s:
                s = s.replace(i, '', 1)
                result += roman_dict[i]
        return result