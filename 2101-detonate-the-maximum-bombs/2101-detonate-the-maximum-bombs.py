class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
        adj = collections.defaultdict(list)
        N = len(bombs)

        for i in range(N):
            x1, y1, r1 = bombs[i]
            for j in range(i+1, N):
                x2, y2, r2 = bombs[j]
                d = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

                if d <= r1: adj[i].append(j)
                if d <= r2: adj[j].append(i)

        def dfs(node):
            if node in visited: return
            visited.add(node)
            for nei in adj[node]:
                if nei not in visited:
                    dfs(nei)


        ans = 0

        for i in range(N):
            visited = set()
            dfs(i)
            ans = max(len(visited), ans)

        return ans
