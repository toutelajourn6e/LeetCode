class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = set('AEIOUaeiou')
        stack = []
        for i in range(len(s)):
            if s[i] in vowels:
                stack.append(s[i])
        for i in range(len(s)):
            if s[i] in vowels:
                s[i] = stack.pop()
        return ''.join(s)