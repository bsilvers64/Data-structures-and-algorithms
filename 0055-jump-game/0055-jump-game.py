class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jump_range = nums[0]

        for i in range(len(nums)):
            if jump_range < nums[i]:
                jump_range = nums[i]
            if i == len(nums)-1: return True
            elif jump_range == 0: return False
            jump_range -= 1
