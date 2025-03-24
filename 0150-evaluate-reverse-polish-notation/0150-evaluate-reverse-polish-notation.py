from operator import add, mul, sub, truediv

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            "+" : add,
            "-" : sub,
            "*" : mul,
            "/" : truediv
        }

        stack = []

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(int(operators[token](num1, num2)))
            
        return stack[-1]