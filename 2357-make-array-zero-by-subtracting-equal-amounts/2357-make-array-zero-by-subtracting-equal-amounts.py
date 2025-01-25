class Solution:
    def find_min_and_reduce(self, arr):
        res = float('inf')
        for i in arr:
            if i != 0: res = min(res, i) 
        if res != float('inf'):
            reduced_arr = [i-res if i != 0 else 0 for i in arr]
            return reduced_arr
        else: return None

    def minimumOperations(self, nums: List[int]) -> int:
        operations = 0
        while nums:
            nums = self.find_min_and_reduce(nums)
            operations += 1
        return operations-1