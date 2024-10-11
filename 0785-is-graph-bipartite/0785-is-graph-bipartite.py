class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        state = [0 for _ in range(len(graph))]

        def bfs(node):
            if state[node]: return True
            q = collections.deque()
            q.append(node)
            state[node] = 1
            while q:
                n = q.popleft()
                for nei in graph[n]:
                    if not state[nei]: 
                        state[nei] = -state[n]
                        q.append(nei)
                    elif state[n] == state[nei]: return False
                        

            return True
        
        for i in range(len(graph)):
            if not bfs(i): return False
        return True