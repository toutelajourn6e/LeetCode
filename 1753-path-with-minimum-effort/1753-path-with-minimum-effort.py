import heapq as hq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
        n, m = len(heights), len(heights[0])
        distance = [[int(1e7)] * m for _ in range(n)]
        distance[0][0] = 0
        q = [(0, 0, 0)]

        while q:
            cost, x, y = hq.heappop(q)
            if x == n-1 and y == m-1:
                return cost

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < m:
                    new_cost = max(cost, abs(heights[x][y] - heights[nx][ny]))
                    if new_cost < distance[nx][ny]:
                        distance[nx][ny] = new_cost
                        hq.heappush(q, (new_cost, nx, ny))

        