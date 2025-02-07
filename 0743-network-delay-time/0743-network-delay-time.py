from heapq import heappush, heappop
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, time in times:
            graph[u].append((v, time))

        min_heap = []
        min_times = defaultdict(int)

        heappush(min_heap, (0, k))

        while min_heap:
            time_to_node, node = heappop(min_heap)
            if node in min_times: continue
            min_times[node] = time_to_node
            for neighbor, time_to_neighbor in graph[node]:
                heappush(min_heap, (time_to_node + time_to_neighbor, neighbor))

        min_time = max(min_times.values())
        if n != len(min_times): return -1

        return min_time