class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = {'(', '{', '['}
        for i in s:
            if i in opening: stack.append(i)
            elif not stack: return False
            else:
                if i == ')' and stack[-1] == '(':
                    stack.pop()
                elif i == '}' and stack[-1] == '{':
                    stack.pop()
                elif i == ']' and stack[-1] == '[':
                    stack.pop()                                      
                else:
                    print(stack[-1], i) 
                    return False
                
        if len(stack) == 0: return True