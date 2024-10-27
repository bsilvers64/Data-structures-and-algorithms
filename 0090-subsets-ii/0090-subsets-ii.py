class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        sub = []
        nums.sort()

        def bk(i):
            if i >= len(nums): 
                ans.append(sub[:])
                return
            
            sub.append(nums[i])
            bk(i+1)
            sub.pop()

            while i + 1 < len(nums) and nums[i] == nums[i+1]: i += 1
            bk(i+1)

        bk(0)
        return ans
