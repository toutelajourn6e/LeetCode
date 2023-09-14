from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        destination = defaultdict(list)

        for ticket in tickets:
            destination[ticket[0]].append(ticket[1])
        for key in destination:
            destination[key].sort(reverse=True)

        def travel(path, visit):
            if not path and visit:
                return visit
            cur = path[-1]
            if not destination[cur]:
                visit.append(path.pop())
                return travel(path, visit)
            next = destination[cur].pop()
            return travel(path + [next], visit)

        return travel(["JFK"], [])[::-1]