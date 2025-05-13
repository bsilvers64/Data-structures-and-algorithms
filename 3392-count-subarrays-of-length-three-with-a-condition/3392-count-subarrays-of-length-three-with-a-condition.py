class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        result = 0

        for r in range(2, len(nums)):
            l, m = r - 2, r - 1
            if (nums[l] + nums[r]) == (nums[m]/2): result += 1

        return result