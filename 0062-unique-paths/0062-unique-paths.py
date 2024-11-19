class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev = [1 for _ in range(n)]
        curr = [1 for _ in range(n)]

        for i in range(1, m):
            for j in range(1, n):
                curr[j] = curr[j-1] + prev[j]
            prev = curr
            curr = [1 for _ in range(n)]

        
        return prev[-1]