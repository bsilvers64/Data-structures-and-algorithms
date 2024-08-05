class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j, ans = 0, 0, 0
        ump = collections.defaultdict(int)

        N = len(s)

        while (i < N):
            ump[s[i]] += 1
            while (i - j + 1 > len(ump)):
                ump[s[j]] -= 1
                if ump[s[j]] == 0: del ump[s[j]]
                j += 1
            ans = max(ans, i - j + 1)             # at the point it would be sure that our condition is satisfied for this window/substring
            i += 1
        return ans