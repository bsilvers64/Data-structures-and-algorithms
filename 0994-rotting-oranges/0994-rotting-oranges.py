class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited = set()
        ans = 0
        q = collections.deque()

        def addNode(r, c):
            if (r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0])
                or (r, c) in visited or grid[r][c] == 0):
                return
            q.append((r, c))
            visited.add((r, c))

        num = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j))
                    visited.add((i, j))
                if grid[i][j] != 0:
                    num += 1
        
        if num == 0: return 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                addNode(r+1, c)
                addNode(r-1, c)
                addNode(r, c+1)
                addNode(r, c-1)
            ans += 1
        
        
        if len(visited) == num:
            return ans-1 
        else: return -1
