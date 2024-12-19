from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        M, N = len(mat), len(mat[0])
        res = [[float('inf')] * N for _ in range(M)]
        q = deque()

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        for i in range(M):
            for j in range(N):
                if mat[i][j] == 0: 
                    res[i][j] = 0
                    q.append((i, j))
          
        while q:
            r, c = q.popleft()
            for i, j in directions:
                nr, nc = r+i, c+j
                if 0 <= nr < M and 0 <= nc < N:
                    if res[nr][nc] > res[r][c] + 1:
                        res[nr][nc] = res[r][c] + 1
                        q.append((nr, nc))

        return res
