class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]
        for i in strs[1:]:
            j, temp = 0, ""
            while j < min(len(res), len(i)):
                if i[j] != res[j]:
                    break
                temp += res[j]
                j+=1
            res = temp
        return res
            