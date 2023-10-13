class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counts = [0] * 26
        for char in ransomNote:
            counts[ord(char) - 97] += 1
        for char in magazine:
            n = ord(char) - 97
            if counts[n] > 0:
                counts[n] -= 1
        return not sum(counts)
