from collections import defaultdict

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def check(string):
            cnt = defaultdict(list)
            for i in range(len(string)):
                cnt[string[i]].append(i)
            return cnt

        for s_list, t_list in zip(check(s).values(), check(t).values()):
            if len(s_list) != len(t_list): return False
            for s_cnt, t_cnt in zip(s_list, t_list):
                if s_cnt != t_cnt: return False
        return True