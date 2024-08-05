class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = j = maxf = 0
        w, ans = 0, 0


        count = collections.defaultdict(int)

        while (j < len(s)):
            w += 1
            count[s[j]] += 1
            maxf = max(maxf, count[s[j]])
            
            while(w - maxf > k):
                count[s[i]] -= 1
                i += 1
                w -= 1

            
            ans = max(ans, w)
            j += 1



        return ans
            