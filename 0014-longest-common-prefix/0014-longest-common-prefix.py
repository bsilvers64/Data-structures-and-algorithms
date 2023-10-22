class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        ans = strs[0]
        if not ans: return ans
        i, j = 0, 0
        print(strs)
        while i < len(strs[0]):
            if strs[0][i] != strs[len(strs)-1][j]:
                return strs[0][:i]
            i+=1
            j+=1 
        print(ans)
        return ans
            