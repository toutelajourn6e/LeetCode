class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map1, map2 = [], []
        for ch in s:
            map1.append(s.index(ch))
        for ch in t:
            map2.append(t.index(ch))
        return True if map1 == map2 else False