class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = []
        for i in range(len(s)):
            if s[i] in ['a', 'e', 'u', 'o', 'i', 'A', 'E', 'U', 'O', 'I']:
                vowels.append(s[i])
        for i in range(len(s)):
            if s[i] in ['a', 'e', 'u', 'o', 'i', 'A', 'E', 'U', 'O', 'I']:
                s[i] = vowels.pop()
        return ''.join(s)