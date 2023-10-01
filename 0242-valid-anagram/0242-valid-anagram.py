from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        dic1, dic2 = defaultdict(int), defaultdict(int)

        for ch1, ch2 in zip(s, t):
            dic1[ch1] += 1
            dic2[ch2] += 1

        for key1, key2 in zip(sorted(dic1.keys()), sorted(dic2.keys())):
            if key1 != key2 or dic1[key1] != dic2[key2]:
                return False
        return True
