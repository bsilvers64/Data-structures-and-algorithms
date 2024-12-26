from operator import add, mul, sub, truediv


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = collections.deque()
        operators = {"+": add, "-": sub, "*": mul, "/": truediv}
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                operand1 = stack.pop()
                operand2 = stack.pop()
                stack.append(int(operators[token](operand2, operand1)))
        
        return stack[0]
