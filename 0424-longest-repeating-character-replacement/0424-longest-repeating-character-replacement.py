from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = defaultdict(int)
        i, j, ans = 0, 0, 0

        N = len(s)
        while(i < N):
            mp[s[i]] += 1
            
            while((i - j + 1) - max(mp.values()) > k):
                mp[s[j]] -= 1
                if not mp[s[j]]: del mp[s[j]]
                j += 1

            ans = max(ans, i - j + 1)
            i += 1
        return ans