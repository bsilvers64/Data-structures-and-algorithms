class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        adj = collections.defaultdict(list)
        for i, e in enumerate(edges):
            adj[i].append(e)
        
        disToN1 = collections.defaultdict()
        disToN2 = collections.defaultdict()
        
        def bfs(node, disMap):
            q = collections.deque()
            q.append([node, 0])

            while q:
                n, dis = q.popleft()
                disMap[n] = dis
                for neighbor in adj[n]:
                    if neighbor != -1 and neighbor not in disMap: 
                        q.append([neighbor, dis+1])
                        
            return
        
        bfs(node1, disToN1)
        bfs(node2, disToN2)

        ans = float('inf')
        res = -1

        for i in range(len(edges)):
            if i in disToN1 and i in disToN2:
                max_dis = max(disToN1[i], disToN2[i])
                if max_dis < ans:
                    ans = max_dis
                    res = i
        
        return res




