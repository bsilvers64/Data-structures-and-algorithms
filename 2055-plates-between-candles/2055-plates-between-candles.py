class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        N = len(s)
        plateSum = [0] * N
        plateCount = 0

        nextCandle, previousCandle = [-1] * N, [-1] * N
        rightMostCandle, leftMostCandle = -1, -1

        for i in range(N):
            if s[i] == "*": 
                plateCount += 1
            elif s[i] == "|":
                leftMostCandle = i
            if s[N-i-1] == "|":
                rightMostCandle = N-i-1

            previousCandle[i] = leftMostCandle
            nextCandle[N-i-1] = rightMostCandle
            plateSum[i] = plateCount

        result = []
        for start, end in queries:
            if start != end and nextCandle[start] < previousCandle[end]:
                result.append(plateSum[previousCandle[end]] - plateSum[nextCandle[start]])
            else:
                result.append(0)

        return result
            