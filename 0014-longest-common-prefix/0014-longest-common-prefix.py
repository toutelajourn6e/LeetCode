class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""

        for i in range(len(strs[0])):
            s = strs[0][i]
            for j in range(len(strs)):
                if len(strs[j]) <= i or strs[j][i] != s: break
            else:
                prefix += s
                continue
            break

        return prefix