class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        check = collections.defaultdict(int)
        for i in range(len(s)):
            if s[i] not in check:
                check[s[i]] = t[i]
            elif t[i] != check[s[i]]:
                return False
        return True