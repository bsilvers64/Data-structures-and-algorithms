class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        M, N = len(grid), len(grid[0])
        time, fresh = 0, 0

        for i in range(M):
            for j in range(N):
                if grid[i][j] == 2: q.append((i, j))
                elif grid[i][j] == 1: fresh += 1
        
        while q and fresh > 0:
            num_rotten = len(q)
            time += 1
            for _ in range(num_rotten):
                i, j = q.pop()
                for r, c in directions:
                    dr, dc = i+r, j+c
                    if 0<=dr<M and 0<=dc<N and grid[dr][dc]==1:
                        grid[dr][dc]=2
                        q.appendleft((dr, dc))
                        fresh -= 1
            
        
        return time if fresh == 0 else -1