class Solution:
    def ispal(self, s, i, j):
        while i < j:
            if s[i] != s[j]: return False
            i += 1
            j -= 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        ans = []
        part = []

        def dfs(i):
            if i >= len(s): 
                ans.append(part[:])
                return
            
            for j in range(i, len(s)):
                if self.ispal(s, i, j):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()

        dfs(0)

        return ans