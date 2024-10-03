class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]: return -1
        M = len(grid)
        directions = [[1, 0], [1, -1], [-1, 0], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1]]
        visited = set()

        q = collections.deque()
        q.append((0, 0, 1))
        visited.add((0, 0))
        
        while q:
            r, c, length = q.popleft()
            if r == M-1 and c == M-1: return length
            for i, j in directions:
                nr, nc = r + i, c + j
                if nr < 0 or nc < 0 or nr >= M or nc >= M or grid[nr][nc] or (nr, nc) in visited:
                    continue
                q.append((nr, nc, length+1))
                visited.add((nr, nc))


        return -1

 
