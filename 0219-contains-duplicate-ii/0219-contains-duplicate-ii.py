class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mp = collections.defaultdict()
        for i, n in enumerate(nums):
            if n in mp:
                if abs(i - mp[n][1] <= k): return True
                else: mp[n][1] = i
            else: mp[n] = [1, i]

        return False