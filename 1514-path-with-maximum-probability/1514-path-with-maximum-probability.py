import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], sp: List[float], start_node: int, end_node: int) -> float:
        graph = collections.defaultdict(list)
        k = 0
        for i, j in edges:
            graph[i].append([j, sp[k]])
            graph[j].append([i, sp[k]])
            k += 1
        
        minheap = [[1, start_node]]
        visit = set()

        while minheap:
            prob, node = heapq.heappop(minheap)
            if node in visit: continue
            visit.add(node)
            #print(node, prob)
            if node == end_node: return -prob
            for nei, p in graph[node]:
                if nei not in visit:
                    temp = prob * p
                    if temp > 0: temp *= -1  
                    else: temp *= 1
                    heapq.heappush(minheap, [temp, nei])
        
        return 0.00