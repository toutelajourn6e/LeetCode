from collections import deque

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        all_visited = (1 << n) - 1
        visited = [[False] * n for _ in range(all_visited + 1)]
        q = deque()

        for node in range(n):
            start_mask = 1 << node
            q.append((node, start_mask, 0))
            visited[start_mask][node] = True

        while q:
            cur, visit, dist = q.popleft()
            if visit == all_visited:
                return dist

            for next in graph[cur]:
                next_mask = visit | (1 << next)
                if not visited[next_mask][next]:
                    q.append((next, next_mask, dist + 1))
                    visited[next_mask][next] = True