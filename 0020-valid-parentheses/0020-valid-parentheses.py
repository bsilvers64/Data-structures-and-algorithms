class Solution:
    def isValid(self, s: str) -> bool:
        
        # maps opening to their respective closing brackets
        brackets = {')': '(', '}': '{', ']':'['}

        stack = []

        for bracket in s:
            # opening bracket - append to stack
            if bracket not in brackets:
                stack.append(bracket)
            # closing bracket - pop from stack
            elif stack and stack[-1] == brackets[bracket]:
                    stack.pop()
            else: 
                # this means no bracket in stack and we are on a closing bracket
                return False
        
        
        return stack == []
