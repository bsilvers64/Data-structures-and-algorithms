class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        visited = set()
        def dfs(index, i, j):
            if index == len(word): return True
            if 0<=i<m and 0<=j<n and board[i][j] == word[index] and (i, j) not in visited:
                visited.add((i, j))
                contains = (dfs(index+1, i+1, j) or
                            dfs(index+1, i, j+1) or
                            dfs(index+1, i-1, j) or
                            dfs(index+1, i, j-1))
                visited.remove((i, j))
                return contains
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(0, i, j): return True
        return False