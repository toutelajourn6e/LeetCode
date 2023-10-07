class Solution:
    def totalNQueens(self, n: int) -> int:
        ans = 0
        
        def n_queen(row, col, left, right):
            nonlocal ans
            if row == n:
                ans += 1
                return

            left <<= 1
            right >>= 1
            impossible = col | left | right

            for i in range(n):
                bit = 1 << i
                if impossible & bit: continue
                n_queen(row + 1, col | bit, left | bit, right | bit)

        n_queen(0, 0, 0, 0)
        return ans