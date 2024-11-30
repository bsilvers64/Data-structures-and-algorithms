class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        res = s = nums[0]

        for i in range(1, len(nums)):
            s += nums[i]
            avg = math.ceil(s/(i+1))
            res = max(res, avg)
        return res