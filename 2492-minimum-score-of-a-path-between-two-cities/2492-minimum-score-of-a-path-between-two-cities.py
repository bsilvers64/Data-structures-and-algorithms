class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        mindis = collections.defaultdict(int)
        adj = collections.defaultdict(list)
        q = collections.deque()
        ans = float('inf')

        for i, j, k in roads:
            adj[i].append([j, k])
            adj[j].append([i, k])

        mindis[1] = 0
        q.append(1)

        while q:
            n = q.popleft()
            for nei, dis in adj[n]:
                if nei != 1:
                    if nei in mindis:
                        mindis[nei] = min(mindis[nei], dis)
                    else:
                        mindis[nei] = dis
                        q.append(nei)
                    ans = min(ans, dis)
        
        return ans



