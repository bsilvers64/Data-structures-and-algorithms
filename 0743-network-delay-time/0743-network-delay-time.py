import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        min_times = collections.defaultdict()
        min_heap = [(0, k)]

        while min_heap:
            time_to_k, node = heapq.heappop(min_heap)
            if node in min_times: continue
            else: 
                min_times[node] = time_to_k
            
            for nei, w in graph[node]:
                if nei not in min_times:
                    heapq.heappush(min_heap, (time_to_k + w, nei))
        

        if len(min_times) == n: return max(min_times.values())
        return -1