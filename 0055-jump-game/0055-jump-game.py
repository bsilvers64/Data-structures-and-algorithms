class Solution:
    def canJump(self, nums: List[int]) -> bool:
        gas = 0
        n = len(nums)
        for i in range(n):
            if nums[i] > gas:
                gas = nums[i]
            if gas == 0 and i != n-1: return False 
            gas -= 1

        return True
