class Solution:
    def decodeString(self, s: str) -> str:
        i = 0
        stack = []
        while i < len(s):
            if s[i] != "]":
                stack.append(s[i])
            else:
                curr_string = ''
                while stack[-1] != "[": 
                    curr_string = stack.pop() + curr_string
                stack.pop()
                count = ''
                while stack and stack[-1].isdigit(): 
                    count = stack.pop() + count
                for _ in range(int(count)): stack.append(curr_string)
            i += 1

        return ''.join(stack)