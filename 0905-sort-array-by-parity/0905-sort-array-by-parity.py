class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        N = len(nums)
        index = 0
        while index < N:
            if nums[index] & 1: break
            index += 1
            
        i = index + 1

        while i < N:
            if nums[i] & 1 == 0:
                nums[index], nums[i] = nums[i], nums[index]
                index += 1
            i += 1
        return nums