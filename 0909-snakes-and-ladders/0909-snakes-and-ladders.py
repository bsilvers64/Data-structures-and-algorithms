class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        def transform(square):
            square -= 1
            r = n - (square // n) - 1
            c = square % n
            if (n*n) % 2:
                if r & 1: c = n - 1 - c
            else:
                if not (r & 1): c = n - 1 - c
            return r, c
        
        q = collections.deque()
        visit = set()

        q.append([1, 0])
        visit.add(1)

        while q:
            num, move = q.popleft()
            for i in range(1, 7):
                nextSquare = num + i
                r, c = transform(nextSquare)
                if board[r][c] != -1:
                    nextSquare = board[r][c]
                if nextSquare == n*n: return move + 1

                if nextSquare not in visit:
                    visit.add(nextSquare)
                    q.append([nextSquare, move+1]) 

        return -1

