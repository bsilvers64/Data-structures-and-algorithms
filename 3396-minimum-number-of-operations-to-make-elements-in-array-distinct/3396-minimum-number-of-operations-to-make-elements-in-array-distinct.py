class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        freq = Counter(nums)
        operations = 0

        def check(freq):
            for i in freq.values():
                if i > 1: return False
            return True

        i = 0
        while not check(freq) and i+2 < len(nums):
            freq[nums[i]] -= 1
            freq[nums[i+1]] -= 1
            freq[nums[i+2]] -= 1
            i += 3
            operations += 1
        
        return operations+1 if not check(freq) else operations