class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        countT, window = defaultdict(int), defaultdict(int)

        for c in t: countT[c] += 1

        res, resLen = [-1, -1], float('inf')
        l = 0
        have, need = 0, len(countT)

        for r in range(len(s)):
            c = s[r]

            window[c] += 1

            if c in countT and countT[c] == window[c]:
                have += 1
            
            while have == need:
                # update max substring length
                if (r-l+1) < resLen:
                    res = [l, r]
                    resLen = (r-l+1)
                
                # decrease window size
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        
        return s[res[0]:res[1]+1]
