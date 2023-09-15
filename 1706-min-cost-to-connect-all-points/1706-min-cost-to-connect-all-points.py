class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]

        def union(a, b):
            if a < b:
                parents[b] = a
            else:
                parents[a] = b

        result = 0
        edges = []
        parents = [i for i in range(len(points))]

        for i, u in enumerate(points):
            for j, v in enumerate(points):
                if i == j: continue
                cost = abs(u[0] - v[0]) + abs(u[1] - v[1])
                edges.append((cost, i, j))

        edges.sort()
        cnt = 0

        for cost, a, b in edges:
            if cnt == len(points) - 1: break
            a_parent = find(a)
            b_parent = find(b)
            if a_parent != b_parent:
                union(a_parent, b_parent)
                result += cost
                cnt += 1

        return result