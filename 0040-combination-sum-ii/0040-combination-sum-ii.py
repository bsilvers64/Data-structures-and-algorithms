class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        sub = []

        def dfs(i, total):
            if target == total:
                res.append(sub[:])
                return
            if i >= len(candidates) or total > target: return

            sub.append(candidates[i])
            dfs(i+1, total+candidates[i])
            sub.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]: i += 1
            dfs(i+1, total)
            

        dfs(0, 0)

        return res