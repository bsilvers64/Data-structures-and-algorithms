class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        res = []
        board = [["." for _ in range(n)] for _ in range(n)]

        columns = set()
        posDiag = set()
        negDiag = set()

        def dfs(r):
            # we have finished all rows and hence found a suitable n-queen placement
            if r == n:
                res.append(["".join(board[i]) for i in range(n)])
                return
            
            # search for a position in all columns
            for c in range(n):
                if c in columns or r+c in posDiag or r-c in negDiag: continue
            
                # found a block so place the queen
                board[r][c] = "Q"
                columns.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)

                # move on to next row
                dfs(r+1)

                # undo operation as we search further columns
                board[r][c] = "."
                columns.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)


        dfs(0)
        return res
