class Solution:
    def check_palindrome(self, s):
        i = 0
        while i < (len(s)//2):
            if s[i] != s[len(s)-i-1]: return False
            i += 1 
        return True

    def partition(self, s: str) -> List[List[str]]:
        
        result = []

        def dfs(index, parts):
            if index >= len(s):
                result.append(parts[:])
                return
            
            for j in range(index, len(s)):
                if self.check_palindrome(s[index:j+1]):
                    parts.append(s[index:j+1])
                    dfs(j+1, parts)
                    parts.pop()

        
        dfs(0, [])

        return result