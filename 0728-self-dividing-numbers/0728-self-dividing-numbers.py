class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []

        for i in range(left, right + 1):
            s = str(i)
            impossible = False
            for ch in s:
                if ch == '0' or i % int(ch):
                    impossible = True
                    break
            if not impossible: ans.append(i)

        return ans