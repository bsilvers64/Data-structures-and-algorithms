class Solution:
    def combinationSum(self, c: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curr, total):
            if total == target: 
                res.append(curr[:])
                return 
            if i >= len(c) or total > target: return 

            curr.append(c[i])
            dfs(i, curr, total+c[i])

            curr.pop()
            dfs(i + 1, curr, total)

        dfs(0, [], 0)

        return res