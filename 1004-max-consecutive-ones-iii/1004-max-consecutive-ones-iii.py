class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxlen = 0
        num_ones = 0

        l, r = 0, 0

        while r < len(nums):
            num_ones += nums[r]

            while (r-l+1) - num_ones > k:
                num_ones -= nums[l]
                l += 1

            maxlen = max(maxlen, (r - l + 1))
            r += 1

        return maxlen 