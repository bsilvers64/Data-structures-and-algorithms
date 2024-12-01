class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        cmap = [0] * 26
        for i in range(len(s)): cmap[ord(s[i])-ord('a')] = i

        res = []
        psize = 0
        maxi = 0

        for i in range(len(s)):
            maxi = max(maxi, cmap[ord(s[i])-ord('a')])
            psize += 1
            if maxi == i:
                res.append(psize)
                maxi = 0
                psize = 0

        return res