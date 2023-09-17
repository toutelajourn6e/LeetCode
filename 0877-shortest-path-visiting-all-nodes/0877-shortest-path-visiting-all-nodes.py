from collections import deque

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        result = []
        all_visited = (1 << len(graph)) - 1
        check = set()

        def bfs(start):
            q = deque()
            q.append((start, 1 << start, 0))

            while q:
                cur, visit, dist = q.popleft()
                if visit == all_visited:
                    return dist
                
                for node in graph[cur]:
                    next = (node, visit | 1 << node, dist + 1)
                    if next not in check:
                        check.add(next)
                        q.append(next)
            
        for i in range(len(graph)):
            result.append(bfs(i))
        
        return min(result)