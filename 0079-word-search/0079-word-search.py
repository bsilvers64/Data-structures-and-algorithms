class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R, C = len(board), len(board[0])
        visited = set()
        def dfs(i, j, k):
            if min(i, j) >= 0 and i < R and j < C and (i, j) not in visited and board[i][j] == word[k]:
                if k == len(word)-1: return True
                visited.add((i, j))
                res = (dfs(i, j+1, k+1) or
                        dfs(i+1, j, k+1) or
                        dfs(i, j-1, k+1) or
                        dfs(i-1, j, k+1))
                visited.remove((i, j))
                return res

        for i in range(R):
            for j in range(C):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0): 
                        print(i, j)
                        return True
                        
        
        return False