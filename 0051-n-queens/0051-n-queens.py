class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        def n_queen(row, col, left, right, path):
            if row == n:
                result.append(tuple(path))
                return

            left <<= 1
            right >>= 1
            impossible = col | left | right

            for i in range(n):
                bit = 1 << i
                if impossible & bit: continue
                
                select = ''
                for j in range(n):
                    if i == j: select += 'Q' 
                    else: select += '.'

                path.append(select)
                n_queen(row + 1, col | bit, left | bit, right | bit, path)
                path.pop()

        n_queen(0, 0, 0, 0, [])
        return result