import sys
sys.setrecursionlimit(10 ** 6)

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]

        def union(a, b):
            a = find(a)
            b = find(b)
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

        for cost, a, b in edges:
            if find(a) != find(b):
                union(a, b)
                result += cost

        return result