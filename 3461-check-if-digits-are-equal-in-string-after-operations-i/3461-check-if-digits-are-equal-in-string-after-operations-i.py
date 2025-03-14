class Solution:
    def hasSameDigits(self, s: str) -> bool:
        n = len(s)
        while n > 2:
            ns = []
            for i in range(n-1):
                ns.append(str((int(s[i]) + int(s[i+1])) % 10))
            s = "".join(ns)
            n -= 1

        return s[0] == s[1]

