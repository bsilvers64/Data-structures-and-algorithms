import heapq

class HeapItem:
    def __init__(self, word, count):
        self.word = word
        self.count = count
    
    def __lt__(self, compareTo):
        if self.count == compareTo.count:
            return self.word > compareTo.word
        return self.count < compareTo.count


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_count = collections.Counter(words)
        heap = []

        for word, count in word_count.items():
            item = HeapItem(word, count)
            if len(heap) < k:
                heapq.heappush(heap, item)
            else:
                if item > heap[0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, item)
        
        res = []
        while k:
            cur = heapq.heappop(heap)
            res.append(cur.word)
            k -= 1
        return res[::-1]

    