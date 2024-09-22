class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ans = 0
        q = collections.deque()

        def addNode(r, c):
            if (r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0])
                or grid[r][c] != 1):
                return
            q.append((r, c))
            grid[r][c] = 2
            nonlocal num
            num -= 1

        num = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j))
                if grid[i][j] == 1:
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
        
        
        return ans-1 if num == 0 else -1
