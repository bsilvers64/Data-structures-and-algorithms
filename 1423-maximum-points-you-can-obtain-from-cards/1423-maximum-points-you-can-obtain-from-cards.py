class Solution:
    def maxScore(self, nums: List[int], k: int) -> int:
        s, i = 0, 0
        k, total = len(nums)-k, sum(nums)
        while k:
            s += nums[i]
            k -= 1
            i += 1
        res = total-s
        j = 0
        while i < len(nums):
            s += nums[i]
            s -= nums[j]
            res = max(res, total-s)
            i += 1
            j += 1
        return res