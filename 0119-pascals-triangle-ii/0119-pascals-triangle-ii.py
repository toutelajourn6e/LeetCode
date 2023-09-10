class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        nums = [0] * (rowIndex + 1)
        nums[0] = 1

        for i in range(rowIndex):
            tmp = 1
            tmp2 = 0
            for j in range(1, i+1):
                tmp2 = nums[j]
                nums[j] += tmp
                tmp = tmp2
            nums[i+1] = 1

        return nums

