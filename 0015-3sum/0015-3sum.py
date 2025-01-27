class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        left = 0
        N = len(nums)
        nums.sort()

        while left < len(nums):
            if nums[left] > 0: break
            elif left > 0 and nums[left] == nums[left-1]:
                left += 1
                continue
            l, r = left+1, N-1

            while l < r:
                total = nums[left]+nums[l]+nums[r]
                if total == 0: 
                    res.append([nums[left], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]: l+=1
                    while l < r and nums[r] == nums[r+1]: r-=1
                elif total > 0:
                    r -= 1
                else: l += 1

            left += 1
        
        return res