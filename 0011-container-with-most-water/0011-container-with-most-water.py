class Solution:
    def maxArea(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        water = 0
        while l < r:
            water = max(water, (r-l)* min(nums[l], nums[r]))
            if nums[l] < nums[r]: l += 1
            else: r -= 1

        return water