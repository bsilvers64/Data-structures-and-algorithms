from heapq import heappush, heappop
class Solution:
    def reorganizeString(self, s: str) -> str:
        heap = []
        freq = Counter(s)

        for char, count in freq.items():
            heappush(heap, [-count, char])

        result = []

        while len(heap) > 1:
            count1, char1 = heappop(heap)
            count2, char2 = heappop(heap)

            result.append(char1)
            result.append(char2)

            count1 += 1
            count2 += 1

            if count1 < 0: heappush(heap, [count1, char1])
            if count2 < 0: heappush(heap, [count2, char2])
        

        if heap:
            if heap[0][0] < -1: return ""
            else:
                result.append(heappop(heap)[1])
        
        
        return "".join(result)




