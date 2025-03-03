class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        N = len(nums)
        for i in range(N):
            if nums[i] < 0: nums[i] = 0
        
        # missing number will lie in the range - [1, len(nums) + 1]
        # so in our array index -i will represent that +ve number i exists
        # len(nums)-1 index will show if len(nums) number exists
        # our worst case is that len(nums)+1 number doesn't exists in the array 
        # which is what we will return in the end

        for i in range(N):
            # get the real +ve number
            val = abs(nums[i])

            # if it is in bounds, we will make val-1 index as -ve to denote this val exists
            if 1 <= val <= N:
                if nums[val-1] == 0:
                    nums[val-1] = -N-1
                elif nums[val-1] > 0:
                    nums[val-1] *= -1
        
        # this performs check for numbers 1 to N
        for i in range(0, N):
            if nums[i] >= 0: return i+1
        
        return N+1
        
