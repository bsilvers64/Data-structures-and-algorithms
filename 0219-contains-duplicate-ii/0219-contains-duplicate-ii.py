class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        indices = {}

        for i, v in enumerate(nums):
            if v in indices and i - indices[v] <= k: return True
            indices[v] = i
        return False