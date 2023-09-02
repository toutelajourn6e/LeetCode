class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dictionary = set(dictionary)
        max_val = len(s) + 1
        dp = [max_val] * (len(s) + 1)
        dp[0] = 0

        for i in range(1, len(s) + 1):
            dp[i] = dp[i-1] + 1
            for j in range(1, i + 1):
                if s[i-j:i] in dictionary:
                    dp[i] = min(dp[i], dp[i-j])
        return dp[-1]