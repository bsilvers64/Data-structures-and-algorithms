class Solution:
    def findCircleNum(self, grid: List[List[int]]) -> int:
        edges = collections.defaultdict(list)
        N = len(grid)

        for i in range(N):
            for j in range(N): 
                if grid[i][j] == 1 and i != j:
                    edges[i+1].append(j+1)
        
        for i in range(1, N+1):
            if i not in edges: edges[i] = set()

        visited = set()
        def dfs(node):
            if node in visited: return
            visited.add(node)
            for n in edges[node]:
                if n not in visited: dfs(n)

        print(edges)
        ans = 0
        
        for i in edges:
            if i not in visited: 
                dfs(i)
                ans += 1

        return ans




        