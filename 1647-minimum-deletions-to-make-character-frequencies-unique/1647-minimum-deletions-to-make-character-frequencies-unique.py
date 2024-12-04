class Solution:
    def minDeletions(self, s: str) -> int:
        charcount = [0] * 26
        used = set()
        for i in s: charcount[ord(i)-ord('a')] += 1

        res = 0
        for i in range(26):
            if charcount[i] == 0: continue
            while charcount[i] > 0 and charcount[i] in used:
                charcount[i] -= 1
                res += 1
            used.add(charcount[i])
        return res