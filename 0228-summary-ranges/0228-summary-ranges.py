class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: return []
        result = []
        start, pre = nums[0], nums[0]

        for i in range(1, len(nums)):
            if not nums[i] == pre + 1:
                if pre == start:
                    result.append(str(start))
                else:
                    result.append(f"{start}->{pre}")
                start = nums[i]
            pre = nums[i]
        else:
            if pre == start:
                    result.append(str(start))
            else:
                result.append(f"{start}->{pre}")
                
        return result