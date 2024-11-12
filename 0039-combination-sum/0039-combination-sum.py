class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        total = 0
        ans = []

        def backtrack(i, temp, total):
            if total == target:
                ans.append(temp[:])
                return
            if i >= len(candidates) or total > target:
                return
            
            temp.append(candidates[i])
            backtrack(i, temp, total+candidates[i])

            temp.pop()
            backtrack(i+1, temp, total)


        backtrack(0, [], 0)
        return ans