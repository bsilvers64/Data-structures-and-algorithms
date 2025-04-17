class Solution:
    def trap(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        left_max, right_max = nums[0], nums[-1]

        water_collected = 0

        while l < r:
            if left_max <= right_max:
                l += 1
                left_max = max(left_max, nums[l])
                water_collected += max(0, left_max - nums[l])
            else:
                r -= 1
                right_max = max(right_max, nums[r])
                water_collected += max(0, right_max - nums[r])


        return water_collected