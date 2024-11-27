class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = 0
        ans_max, ans_min = float("-inf"), float("inf")
        curr1, curr2 = 0, 0

        for i in nums:
            curr1 += i
            curr2 += i
            total += i
            ans_max = max(ans_max, curr1)
            ans_min = min(ans_min, curr2)
            if curr1 < 0: curr1 = 0
            if curr2 > 0: curr2 = 0
        

        return ans_max if total==ans_min else max(ans_max, total-ans_min)