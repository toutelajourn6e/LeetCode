# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start, end = 1, n
        first = int(1e10)

        while start <= end:
            mid = (start + end) // 2
            if isBadVersion(mid):
                end = mid - 1
                first = min(first, mid)
            else:
                start = mid + 1
        return first