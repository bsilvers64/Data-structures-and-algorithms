class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        result = []
        N = len(s)
        
        prefixSum = [0] * N
        nextPlate = [-1] * N
        previousPlate = [-1] * N

        count = 0
        lastPlateIndex1, lastPlateIndex2 = -1, -1

        for i in range(N):
            if s[i] == "|": lastPlateIndex1 = i
            previousPlate[i] = lastPlateIndex1

            if s[N-i-1] == "|": lastPlateIndex2 = N-i-1
            nextPlate[N-i-1] = lastPlateIndex2

            if s[i] == "*": count += 1
            prefixSum[i] = count

        for query in queries:
            start = query[0]
            end = query[1]

            firstPlate = nextPlate[start]
            lastPlate = previousPlate[end]
            
            result.append(prefixSum[lastPlate] - prefixSum[firstPlate]) if (firstPlate < lastPlate and start!=end) else result.append(0)

        return result