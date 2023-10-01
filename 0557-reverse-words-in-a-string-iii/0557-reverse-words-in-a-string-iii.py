class Solution:
    def reverseWords(self, s: str) -> str:
        result = []
        for string in s.split():
            result.append(string[::-1])
        return ' '.join(result)