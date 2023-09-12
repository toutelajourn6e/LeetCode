from collections import defaultdict

class Solution:
    def minDeletions(self, s: str) -> int:
        frequency = defaultdict(int)
        ans = 0

        for ch in s:
            frequency[ch] += 1
        
        freq_set = set()
        for val in frequency.values():
            while val > 0:
                if val not in freq_set:
                    freq_set.add(val)
                    break
                else:
                    val -= 1
                    ans += 1

        return ans