class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        mp = [0] * 2
        for i in nums:
            if i != 2: mp[i] += 1
        
        for i in range(len(nums)):
            if mp[0]: 
                nums[i] = 0
                mp[0] -= 1
            elif mp[1]:
                nums[i] = 1
                mp[1] -= 1
            else:
                nums[i] = 2
                

