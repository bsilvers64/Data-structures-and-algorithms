class Solution:
    def totalNQueens(self, n: int) -> int:
        boards = 0
        cols, posDiag, negDiag = set(), set(), set()

        def dfs(r):
            nonlocal boards
            if r == n:
                boards += 1
                return
            
            for c in range(n):
                if c in cols or r+c in posDiag or r-c in negDiag: continue
                cols.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)

                dfs(r+1)

                cols.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)


        dfs(0)
        return boards