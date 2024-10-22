class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        r, l = 0, 0
        while r < len(nums):
            count = 1
            while r + 1 < len(nums) and nums[r] == nums[r+1]:
                r += 1
                count += 1
            
            steps = min(2, count)
            k = 0
            while k < steps:
                nums[l] = nums[r]
                l += 1
                k += 1
            r += 1
        return l