class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        win = set()

        i = 0
        for j in range(len(nums)):
            if abs(j - i) > k:
                win.remove(nums[i])
                i += 1
            win.add(nums[j]) 
            if len(win) != (j-i+1): return True
        return False