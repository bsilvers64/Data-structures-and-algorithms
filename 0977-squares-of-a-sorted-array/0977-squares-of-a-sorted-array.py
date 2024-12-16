class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res = [0] * N
        maxIndex = N-1
        l, r = 0, N-1

        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                res[maxIndex] = pow(nums[l], 2)
                l += 1
            else:
                res[maxIndex] = pow(nums[r], 2)
                r -= 1
            maxIndex -= 1                

        return res