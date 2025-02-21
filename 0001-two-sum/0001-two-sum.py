class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = collections.defaultdict()
        for i, k in enumerate(nums):
            if target-k in index_map and i != index_map[target-k]: return [i, index_map[target-k]]
            else: index_map[k] = i
        