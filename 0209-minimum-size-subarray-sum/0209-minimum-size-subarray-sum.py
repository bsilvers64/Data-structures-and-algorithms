class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = len(nums)+1
        i, j, s = 0, 0, 0
        while j < len(nums):
            if s < target:
                s += nums[j]
                while (s >= target):
                    ans = min(ans, j - i + 1)
                    s -= nums[i]
                    i += 1
                j += 1
            print(i, j)
        return 0 if ans == len(nums) + 1 else ans