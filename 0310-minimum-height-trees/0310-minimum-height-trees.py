class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = collections.defaultdict(list)
        deg = collections.defaultdict(int)
        if n == 1: return [0]
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)
            deg[i] += 1
            deg[j] += 1
        
        q = collections.deque()

        for i in range(n):
            if deg[i] == 1: q.append(i)
        
        while len(deg) > 2:
            N = len(q)
            while N:
                n = q.popleft()
                del deg[n]
                
                for nei in adj[n]:
                    deg[nei] -= 1
                    if deg[nei] == 1: 
                        q.append(nei)
                N -= 1
        
        ans = []
        while q:
            ans.append(q.pop())
        
        return ans


        
        


