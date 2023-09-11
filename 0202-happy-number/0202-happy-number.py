class Solution:
    def isHappy(self, n: int) -> bool:
        check_loop = set()
        n = str(n)
        flag = True

        while flag:
            flag = False
            n = sum([int(i) * int(i) for i in n])

            if n in check_loop: return False
            else: check_loop.add(n)

            n = str(n)
            if n.count('1') != 1: flag = True
            else:
                for i in n:
                    if i not in ['0', '1']: flag = True

        return True
