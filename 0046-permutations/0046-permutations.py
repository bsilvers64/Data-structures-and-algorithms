class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        sub = []

        def bk():
            if len(nums) == len(sub):
                ans.append(sub[:])
                return
            
            for k in nums:
                if k not in sub:
                    sub.append(k)
                    bk()
                    sub.pop()
        
        bk()

        return ans