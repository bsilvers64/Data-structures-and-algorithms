class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minl, ans = 201, []
        for i in strs:
            minl = min(minl, len(i))

        if minl == 0: return ""
        elif len(strs) == 1: return strs[0]

        k = 0
        for i in range(0, minl):
            for j in range(1, len(strs)):
                if strs[j][i] != strs[k][i]: return "".join(ans)
                k += 1
            ans.append(strs[k][i])
            k = 0

        return ''.join(ans)