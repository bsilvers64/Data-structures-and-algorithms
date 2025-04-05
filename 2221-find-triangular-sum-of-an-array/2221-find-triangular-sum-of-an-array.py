class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        times = len(nums)-1
        
        for _ in range(times):
            temp = []
            for i in range(len(nums)-1):
                temp.append((nums[i]+nums[i+1])%10)
            nums = temp
            
        return nums[-1]