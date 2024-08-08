class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i, j, ans = 0, 0, float('inf')

        window_sum = 0

        N = len(nums)

        while (i < N):
            window_sum += nums[i]
            while (window_sum >= target):
                ans = min(ans, i - j + 1)
                window_sum -= nums[j]
                j += 1
            i += 1

        return 0 if ans == float('inf') else ans