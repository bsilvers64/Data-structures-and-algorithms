class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        visited = set()
        adj = collections.defaultdict(list)

        for i, j in edges:
            adj[i].append(j)

        flag = 0
        def dfs(node):
            nonlocal flag
            if node in visited: return
            visited.add(node)
            for nei in adj[node]:
                if nei in visited: ans.discard(nei)
                if nei not in visited: dfs(nei)
        
        ans = set()

        for i in range(n):
            if i not in visited: 
                dfs(i)
                ans.add(i)
        
        return list(ans)

