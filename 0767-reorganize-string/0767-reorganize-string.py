from heapq import heappush, heappop

class Solution:
    def reorganizeString(self, s: str) -> str:
        heap = []

        character_count = Counter(s)

        # push -> [charcter's frequency, charcter] in the heap
        for character, count in character_count.items():
            heappush(heap, [-count, character])

        result_string = []

        while len(heap) >= 2:
        
            # extract 2 characters from the heap
            count1, character1 = heappop(heap)
            count2, character2 = heappop(heap)

            # append these characters one-by-one
            result_string.append(character1)
            result_string.append(character2)

            # after using these characters check their count, and if its still left,
            # push to heap with count decreased by 1
            if count1 + 1 < 0:
                heappush(heap, [count1 + 1, character1])
            
            if count2 + 1 < 0:
                heappush(heap, [count2 + 1, character2])



        # if the remaining character's count is more than 1
        # OR it is same as last appended charcter to result string, our string is not possible
        if heap:
            if heap[0][0] < -1 or (result_string and result_string[-1] == heap[0][1]): 
                return ""

            result_string.append(heappop(heap)[1])

        return ''.join(result_string)


