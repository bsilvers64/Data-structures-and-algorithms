class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        k = 0
        n = len(matrix)
        for i in range(0, n):
            for j in range(0, k):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            k += 1
        print(matrix)
        for i in range(0, n):
            for j in range(0, n//2):
                matrix[i][j], matrix[i][n-j-1] = matrix[i][n-j-1], matrix[i][j]
