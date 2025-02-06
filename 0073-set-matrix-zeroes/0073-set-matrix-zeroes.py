class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        flag_row = 0
        flag_col = 0

        M, N = len(matrix), len(matrix[0])

        for i in range(N): 
            if matrix[0][i] == 0: flag_row = 1
        
        for i in range(M):
            if matrix[i][0] == 0: flag_col = 1

        
        for i in range(1, M):
            for j in range(1, N):
                if matrix[i][j] == 0: 
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        
        for i in range(1, M):
            if matrix[i][0] == 0:
                for j in range(1, N):
                    matrix[i][j] = 0

        for j in range(1, N):
            if matrix[0][j] == 0:
                for i in range(1, M):
                    matrix[i][j] = 0
        
        if flag_col:
            for i in range(M): matrix[i][0] = 0
        if flag_row:
            for j in range(N): matrix[0][j] = 0