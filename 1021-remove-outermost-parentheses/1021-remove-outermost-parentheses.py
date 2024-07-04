class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        no_include = [0] * len(s)
        stack =  []

        for i, op in enumerate(s):
            if op == "(":
                stack.append(i)
            else:
                index = stack.pop()
            
            if not stack:
                no_include[index] = 1
                no_include[i] = 1
        
        ans = []
        for i in range(len(s)):
            if not no_include[i]:
                ans.append(s[i])

        return ''.join(ans)
                
