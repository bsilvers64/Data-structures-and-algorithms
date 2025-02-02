class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        M, N = len(matrix), len(matrix[0])
        for i in range(M):
            for j in range(i+1):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(M):
            for j in range(N//2):
                matrix[i][j], matrix[i][N-j-1] = matrix[i][N-j-1], matrix[i][j]
                
