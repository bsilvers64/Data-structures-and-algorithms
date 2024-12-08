class Solution:
    def longestPalindrome(self, s: str) -> int:
        cmap = collections.defaultdict(int)
        ans = 0
        for i in s: cmap[i] += 1
        odd_exists = False
        for v in cmap.values():
            if v % 2 == 0: ans += v
            else:
                odd_exists = True
                ans += (v-1)
        
        return ans + 1 if odd_exists else ans