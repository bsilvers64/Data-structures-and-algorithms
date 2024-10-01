class Solution:
    def checkMove(self, board: List[List[str]], rM: int, cM: int, color: str) -> bool:
        R, C = len(board), len(board[0])
        directions = [[1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1]]
        
        def check(r, c, i, j):
            print(r, c, i, j)
            if (r >= 0 and c >= 0 and r < R and c < C):
                if board[r][c] == board[rM][cM]: return True
                elif board[r][c] == ".": return False
                return check(r+i, c+j, i, j)
            else:
                return False
        
        board[rM][cM] = color
        for i, j in directions:
            r, c = rM + i, cM + j
            if (r >= 0 and c >= 0 and r < R and c < C and 
                board[r][c] != board[rM][cM] and board[r][c] != "."):
                if check(r, c, i, j): return True
        
        return False

