class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        l, r = 0, 0
        res = []
        while l < len(nums) or r < len(nums):
           
            while l < len(nums) and nums[l] < 0: l += 1
            if l < len(nums) and nums[l] > 0: 
                res.append(nums[l])
                l += 1
           
            while r < len(nums) and nums[r] > 0: r += 1
            if r < len(nums) and nums[r] < 0: 
                res.append(nums[r])      
                r += 1      

        return res