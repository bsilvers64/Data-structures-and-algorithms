class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivot = None
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]: 
                pivot = i
                break
        else:
            nums.reverse() 
            return 

        for i in range(len(nums)-1, -1, -1):
            if nums[i] > nums[pivot]:
                nums[i], nums[pivot] = nums[pivot], nums[i]
                break

        nums[pivot+1::] = reversed(nums[pivot+1::])
        
        