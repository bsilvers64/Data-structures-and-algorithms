class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red, blue = collections.defaultdict(list), collections.defaultdict(list)
        for i, j in redEdges:
            red[i].append(j)
        for i, j in blueEdges:
            blue[i].append(j)
        visit = set()
        ans = [-1 for i in range(n)]

        q = collections.deque()
        q.append([0, 0, None])

        visit.add((0, None))

        ## R - 1, B - 0

        while q:
            node, dis, color = q.popleft()
            # print(node, color)
            if ans[node] == -1: ans[node] = dis
            if color != 1:
                for n in red[node]:
                    if (n, 1) not in visit:
                        q.append([n, dis+1, 1])
                        visit.add((n, 1))
            if color != 0:
                for n in blue[node]:
                    if (n, 0) not in visit:
                        q.append([n, dis+1, 0])
                        visit.add((n, 0))               

        return ans