class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        M, N = len(board), len(board[0])
        def dfs(i, j):
            if 0 <= i < M and 0 <= j < N and board[i][j] == "O":
                board[i][j] = "T"
                dfs(i, j+1)
                dfs(i+1, j)
                dfs(i, j-1)
                dfs(i-1, j)
        
        for i in range(M):
            if board[i][0] == "O": dfs(i, 0)
            if board[i][N-1] == "O": dfs(i, N-1)

        for i in range(N):
            if board[0][i] == "O": dfs(0, i)
            if board[M-1][i] == "O": dfs(M-1, i)

        for i in range(M):
            for j in range(N):
                if board[i][j] == "O": board[i][j] = "X" 

        for i in range(M):
            for j in range(N):
                if board[i][j] == "T": board[i][j] = "O" 
    