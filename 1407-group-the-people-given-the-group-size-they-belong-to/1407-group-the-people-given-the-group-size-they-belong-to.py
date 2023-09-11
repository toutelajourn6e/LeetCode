from collections import defaultdict

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        group = defaultdict(list)
        ans = []

        for i in range(len(groupSizes)):
            group_num = groupSizes[i]
            if len(group[group_num]) == group_num:
                ans.append(group[group_num][:])
                group[group_num].clear()
            group[group_num].append(i)
        
        for key in group:
            if group[key]:
                ans.append(group[key][:])

        ans.sort(key=len)
        return ans