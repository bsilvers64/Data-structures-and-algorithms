class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        blue, red = set(), set()

        def bfs(node):
            if node in blue or node in red: return True
            q = collections.deque()
            q.append(node)
            blue.add(node)
            while q:
                n = q.popleft()
                bl = True if n in blue else False
                for nei in graph[n]:
                    if bl and nei in blue: return False
                    elif not bl and nei in red: return False
                    elif nei not in red and nei not in blue:
                        if bl:
                            red.add(nei)
                        else:
                            blue.add(nei)
                        q.append(nei)

            return True
        
        for i in range(len(graph)):
            if not bfs(i): return False
        return True