class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)

        k = 0
        for l1, l2 in equations:   
            graph[l1].append([l2, values[k]])
            graph[l2].append([l1, (1/values[k])])
            k += 1
        
        def bfs(src, dest):
            if src not in graph or dest not in graph: return -1
            if src == dest: return 1

            q = deque()
            visit = set()
            q.appendleft([src, 1])
            visit.add(src)

            while q:
                node, val = q.pop()
                if node == dest: return val
                for neighbor, d in graph[node]:
                    if neighbor not in visit:
                        visit.add(neighbor)
                        q.appendleft([neighbor, val * d])

            return -1

        return [bfs(src, dst) for src, dst in queries]