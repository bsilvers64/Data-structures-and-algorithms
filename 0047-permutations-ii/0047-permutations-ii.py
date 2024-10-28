class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        mp = {i:0 for i in nums}
        for i in nums:
            mp[i] += 1

        ans = []
        sub = []

        def dfs():
            if len(sub) == len(nums):
                ans.append(sub[:])
                return
            
            for i in mp:
                if mp[i] > 0:
                    sub.append(i)
                    mp[i] -= 1
                    dfs()
                    sub.pop()
                    mp[i] += 1

        dfs()
        return ans