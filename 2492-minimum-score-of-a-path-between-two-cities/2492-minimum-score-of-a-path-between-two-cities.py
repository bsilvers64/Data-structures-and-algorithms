from collections import deque, defaultdict

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)
        
        # Build adjacency list
        for a, b, d in roads:
            adj[a].append((b, d))
            adj[b].append((a, d))
        
        # BFS to traverse all reachable cities from city 1
        visited = set()
        q = deque([1])
        visited.add(1)
        min_score = float('inf')
        
        while q:
            city = q.popleft()
            
            for neighbor, distance in adj[city]:
                min_score = min(min_score, distance)  # Update minimum distance on any path
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)
        
        return min_score
