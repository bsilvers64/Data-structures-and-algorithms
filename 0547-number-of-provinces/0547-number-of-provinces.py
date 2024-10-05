class Solution:
    def findCircleNum(self, grid: List[List[int]]) -> int:
        edges = []
        N = len(grid)
        par = [i for i in range(N+1)]
        rank = [1] * (N+1)

        for i in range(N):
            for j in range(i + 1, N): 
                if grid[i][j] == 1:
                    edges.append([i+1, j+1])

        def find(node):
            n = node

            while (n != par[n]):
                n = par[n]
            
            while (n != node):
                temp = par[node]
                par[node] = n
                node = temp

            return n
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2: return 0
            
            if rank[p1] > rank[p2]:
                rank[p1] += rank[p2]
                par[p2] = par[p1]
            else:
                rank[p2] += rank[p1]
                par[p1] = par[p2]

            return 1
        
        ans = N
        
        for i, j in edges:
            if union(i, j): ans -= 1

        return ans




        