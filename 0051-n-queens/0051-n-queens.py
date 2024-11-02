class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        posdig = set()
        negdig = set()
        col = set()

        board = [["."] * n for i in range(n)]
        ans = []

        def backtrack(r):
            if r == n:
                copy = [row for row in board]
                ans.append(["".join(row) for row in copy])
                return 
            
            # iterating through all columns for row - r
            for c in range(n):
                if c in col or (r+c) in posdig or (r-c) in negdig: continue
                col.add(c)
                posdig.add(r+c)
                negdig.add(r-c)
                board[r][c] = "Q"

                backtrack(r+1)

                col.remove(c)
                posdig.remove(r+c)
                negdig.remove(r-c)
                board[r][c] = "."


        backtrack(0)

        return ans