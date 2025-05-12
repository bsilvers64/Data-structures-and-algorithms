class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = defaultdict(int)
        result = 0

        l, r = 0, 0
        while r < len(s):
            count[s[r]] += 1
            while len(count) != (r-l+1):
                count[s[l]] -= 1
                if count[s[l]] == 0: 
                    del count[s[l]]
                l += 1
            result = max(result, r-l+1)
            r += 1

        return result