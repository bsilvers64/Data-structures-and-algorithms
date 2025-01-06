class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s): return []
        countP, countS = defaultdict(int), defaultdict(int)
        for i in range(len(p)):
            countP[p[i]] += 1
            countS[s[i]] += 1
        
        res = [0] if countP == countS else []

        l = 0
        for r in range(len(p), len(s)):
            countS[s[l]] -= 1
            countS[s[r]] += 1

            if countS[s[l]] <= 0:
                del countS[s[l]]

            l += 1
            if countP == countS: res.append(l)

        return res