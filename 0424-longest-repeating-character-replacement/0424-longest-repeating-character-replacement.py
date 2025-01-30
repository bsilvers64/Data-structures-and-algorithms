class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        l, r = 0, 0
        freq = defaultdict(int)
        while r < len(s):
            freq[s[r]] += 1
            while (r-l+1) - max(freq.values()) > k:
                freq[s[l]] -= 1
                if not freq[s[l]]: del freq[s[l]]
                l += 1
            max_len = max(max_len, r-l+1)
            r += 1

        return max_len