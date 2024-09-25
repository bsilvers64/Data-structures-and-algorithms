class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        neighbors = collections.defaultdict(list)
        for i, j in connections:
            neighbors[i].append(j)
            neighbors[j].append(i)
        connections = {(i, j) for i, j in connections}
        
        def bfs(root):
            nonlocal neighbors, connections, change
            q = collections.deque()
            visit = set()
            visit.add(root)
            q.append(root)
            while q:
                node = q.popleft() 
                for n in neighbors[node]:
                    if n in visit: continue
                    if (n, node) not in connections: change += 1
                    visit.add(n)
                    q.append(n)
    

        change = 0
        bfs(0)

        return change