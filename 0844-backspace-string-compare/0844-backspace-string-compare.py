class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def nextValidChar(str, index):
            backspaces = 0
            while index >= 0:
                if backspaces == 0 and str[index] != "#": break
                elif str[index] == "#":
                    backspaces += 1
                else:
                    backspaces -= 1
                index -= 1
            return index

        i, j = len(s)-1, len(t)-1

        while i >= 0 or j >= 0:
            i = nextValidChar(s, i)
            j = nextValidChar(t, j)
            ci = s[i] if i >= 0 else ""
            cj = t[j] if j >= 0 else ""
            if ci != cj: return False
            i -= 1
            j -= 1
        return True