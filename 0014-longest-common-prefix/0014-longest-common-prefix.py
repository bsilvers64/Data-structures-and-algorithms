class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        if len(strs[0]) == 0: return strs[0]
        print(strs)
        i = 0
        while i < len(strs[0]):
            if strs[0][i] != strs[-1][i]: return strs[0][:i]
            i+=1
        return strs[0][:i]