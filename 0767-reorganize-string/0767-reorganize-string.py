from heapq import heappush, heappop
class Solution:
    def reorganizeString(self, s: str) -> str:
        count = defaultdict(int)
        for char in s:
            count[char] += 1

        heap = []
        for char, freq in count.items():
            heappush(heap, [-freq, char])

        result_string = []

        while len(heap) >= 2:
            count1, char1 = heappop(heap)
            count2, char2 = heappop(heap)

            result_string.append(char1)
            result_string.append(char2)

            count1 += 1
            count2 += 1

            if count1 < 0: heappush(heap, [count1, char1])
            if count2 < 0: heappush(heap, [count2, char2])
        
        if heap:
            if -heap[0][0] > 1 or (result_string and heap[0][1] == result_string[-1]): return ""
            else:
                result_string.append(heappop(heap)[1])
        
        return "".join(result_string)
            


