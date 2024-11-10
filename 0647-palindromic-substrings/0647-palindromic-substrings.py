class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        N = len(s)
        for i in range(N):
            l, r = i, i

            while l >= 0 and r < N and s[l] == s[r]:
                ans += 1
                l -= 1
                r += 1
            
            l, r  = i, i+1

            while l >= 0 and r < N and s[l] == s[r]:
                ans += 1
                l -= 1
                r += 1


        return ans