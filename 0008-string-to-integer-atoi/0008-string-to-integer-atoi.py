class Solution:
    def myAtoi(self, s: str) -> int:
        state, value, i, sign = 0, 0, 0, 1

        if not len(s): return 0

        while i < len(s):
            char = s[i]
            if state == 0:
                if char.isdigit():
                    state = 2
                    value = value * 10 + int(char)
                elif char == " ":
                    state == 0
                elif char == "+" or char == "-":
                    state = 1
                    sign = 1 if char == "+" else -1
                else:
                    return 0
            elif state == 1:
                if char.isdigit():
                    state = 2
                    value = value * 10 + int(char)
                else:
                    return 0
            elif state == 2:
                if char.isdigit():
                    state = 2
                    value = value * 10 + int(char)
                else:
                    break

            i += 1

        value *= sign
        value = min(2**31-1, value)
        value = max(-(2**31), value)   
        return value             