class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(pattern) != len(s): return False
        
        patterns = {}
        used = set()
        for p, word in zip(pattern, s):
            if p not in patterns and word not in used:
                patterns[p] = word
                used.add(word)
            if p not in patterns or patterns[p] != word:
                return False
        return True
