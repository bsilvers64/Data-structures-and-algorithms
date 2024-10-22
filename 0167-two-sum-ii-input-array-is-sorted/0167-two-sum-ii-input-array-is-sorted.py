class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mp = collections.defaultdict(int)
        for i, v in enumerate(numbers):
            if target - v in mp:
                return [mp[target-v], i + 1]
            else:
                mp[v] = i + 1
        