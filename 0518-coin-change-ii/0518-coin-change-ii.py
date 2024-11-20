class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def dfs(i, a):
            if (i, a) in memo: return memo[(i, a)]
            if i >= len(coins) or a > amount: return 0
            if a == amount: return 1

            memo[(i, a)] = dfs(i, a + coins[i]) + dfs(i+1, a)
            return memo[(i, a)]
        
        return dfs(0, 0)