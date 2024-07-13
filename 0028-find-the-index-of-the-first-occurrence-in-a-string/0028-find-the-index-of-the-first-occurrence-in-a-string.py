class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)
        if n > m: return -1
        if n == m: return 0 if needle == haystack else -1

        
        def get_lps(needle):
            lps = [0] * len(needle)
            i, j = 1, 0
            while i < len(needle):
                if needle[i] == needle[j]: 
                    j += 1
                    lps[i] = j
                    i += 1
                elif j > 0:
                    j = lps[j-1]
                else:
                    lps[i] = 0
                    i += 1
            return lps
        
        i, j = 0, 0
        lps = get_lps(needle)

        while i < m and j < n:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            elif j > 0:
                j = lps[j-1]
            else:
                i += 1
        
        # this will return 1st occurance as when the string matches first, it will lead to 
        # the j hitting == n so loop end
        
        return -1 if j < n else i-n