from collections import Counter

class Solution:
    def minDeletions(self, s: str) -> int:
        frequency = Counter(s)
        ans = 0
        
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