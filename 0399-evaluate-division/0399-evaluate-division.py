class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = collections.defaultdict(list)
        k = 0
        for i, j in equations:
            adj[i].append([j, values[k]])
            adj[j].append([i, 1/values[k]])
            k += 1
        
        def bfs(start, dest):
            if start not in adj or dest not in adj: return -1
            if start == dest: return 1

            q = collections.deque()
            v = set()
            v.add(start)
            q.append([start, 1])
            ans = 0

            while q:
                n, val = q.popleft()
                if n == dest: return val
                for nei, div in adj[n]:
                    
                    if nei not in v: 
                        q.append([nei, div*val])
                        v.add(nei)

            return -1
            
        return [bfs(q[0], q[1]) for q in queries]