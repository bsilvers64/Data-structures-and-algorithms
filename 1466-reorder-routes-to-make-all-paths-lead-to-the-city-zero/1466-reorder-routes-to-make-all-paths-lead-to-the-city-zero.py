class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        neighbors = defaultdict(list)
        for i, j in connections:
            neighbors[i].append(j)
            neighbors[j].append(i)

        routes = {(i, j) for i, j in connections}

        queue = deque()
        visited = set()
        change = 0

        queue.append(0)
        visited.add(0)

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                for neighbor in neighbors[node]:
                    if neighbor in visited: continue
                    visited.add(neighbor)
                    queue.appendleft(neighbor)
                    if (neighbor, node) not in routes: change += 1

        return change