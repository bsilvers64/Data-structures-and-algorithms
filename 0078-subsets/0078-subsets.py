class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        sub = []
        def dfs(i, sub):
            if i == len(nums):
                ans.append(sub[:])
                return
            
            sub.append(nums[i])
            dfs(i+1, sub)
            sub.pop()
            dfs(i+1, sub)

        
        dfs(0, sub)
        return ans