class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        temp = 0
        ans = float('-inf')
        for i in nums:
            temp += i
            ans = max(temp, ans)
            if temp < 0: temp = 0

        return ans