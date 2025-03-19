class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        times = len(nums)-1
        while times > 0:
            temp = []
            for i in range(times):
                temp.append((nums[i] + nums[i+1]) % 10)
            nums = temp
            times -= 1
        return nums[-1]