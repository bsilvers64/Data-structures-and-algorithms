class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        memo = {}
        stoneSum = sum(stones)
        target = ceil(stoneSum/2)

        def dfs(i, total):
            if (i, total) in memo: return memo[(i, total)]
            if i >= len(stones) or total >= target: 
                return abs(total - (stoneSum - total))

            memo[(i, total)] = min(dfs(i+1, total+stones[i]), dfs(i+1, total))
            return memo[(i, total)]
        
        return dfs(0, 0)