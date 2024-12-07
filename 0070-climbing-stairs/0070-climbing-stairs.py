class Solution:
    def climbStairs(self, n: int) -> int:
        mem = collections.defaultdict()
        def dfs(i):
            if i in mem: return mem[i]
            if i == n: return 1
            elif i > n: return 0
            mem[i] = dfs(i+1) + dfs(i+2)
            return mem[i]
        return dfs(0)