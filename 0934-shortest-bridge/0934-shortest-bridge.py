class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        visit = set()
        N = len(grid)
        direct = [[1, 0], [0, -1], [-1, 0], [0, 1]]

        def invalid(r, c):
            if r < 0 or c < 0 or r >= N or c >= N: return True
            return False
        
        def dfs(r, c):
            if invalid(r, c) or (r, c) in visit or not grid[r][c]: return
            visit.add((r, c))
            for dr, dc in direct:
                dfs(r + dr, c + dc)

        def bfs():
            res, q = 0, collections.deque(visit)
            while q:
                layer = len(q)
                for _ in range(layer):
                    r, c = q.popleft()
                    for dr, dc in direct:
                        if invalid(r + dr, c + dc) or (r+dr, c+dc) in visit: continue
                        if grid[r+dr][c+dc]: return res
                        q.append((r + dr, c + dc))
                        visit.add((r + dr, c + dc))
                res += 1
            return res

        for r in range(N):
            for c in range(N):
                if grid[r][c]:
                    dfs(r, c)
                    return bfs()

