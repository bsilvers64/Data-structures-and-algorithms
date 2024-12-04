class Solution:
    def minDeletions(self, s: str) -> int:
        charcount = [0] * 26
        for i in s: charcount[ord(i)-ord('a')] += 1
        res = 0

        charcount.sort()

        for i in range(24, -1, -1):
            if charcount[i] == 0: break

            if charcount[i] >= charcount[i+1]:
                prev = charcount[i]
                charcount[i] = max(0, charcount[i+1]-1)
                res += prev - charcount[i]

        return res