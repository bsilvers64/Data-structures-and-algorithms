import heapq
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0: return False

        count = collections.defaultdict(int)
        for i in hand: count[i] += 1

        minh = list(count.keys())
        heapq.heapify(minh)
        while minh:
            first = minh[0]
            for i in range(first, first+groupSize):
                
                if i not in count: return False
                count[i] -= 1
                if count[i] == 0:
                    if minh[0] != i: return False
                    heapq.heappop(minh) 
        return True