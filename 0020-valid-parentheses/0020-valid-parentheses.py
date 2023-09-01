class Solution:
    def isValid(self, s: str) -> bool:
        dic = {')': '(', '}': '{', ']': '['}
        stack = []

        for i in s:
            if i not in dic.keys():
                stack.append(i)
            else:
                if not stack or stack[-1] != dic[i]: return False
                stack.pop()

        return not stack        