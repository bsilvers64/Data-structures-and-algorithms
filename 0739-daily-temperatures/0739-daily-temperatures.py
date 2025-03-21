class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                _, index = stack.pop()
                result[index] = i-index
            stack.append([temp, i])

        while stack:
            _, i = stack.pop()
            result[i] = 0

        return result