import collections
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        score = Counter(nums)
        nums = sorted(list(set(nums)))

        dp0, dp1 = 0, 0

        for i in range(len(nums)):
            curEarn = nums[i] * score[nums[i]]
            if i > 0 and nums[i] == nums[i - 1] + 1:
                temp = dp1
                dp1 = max(curEarn + dp0, dp1)
                dp0 = temp
            else:
                temp = dp1
                dp1 = curEarn + dp1
                dp0 = temp
        return dp1
