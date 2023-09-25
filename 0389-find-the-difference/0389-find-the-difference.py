class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dic = {}

        for ch in s:
            dic[ch] = dic.get(ch, 0) + 1
        
        for ch in t:
            if ch not in dic:
                return ch
            else:
                dic[ch] = dic.get(ch) - 1
                if dic[ch] == 0:
                    del dic[ch]
            
        