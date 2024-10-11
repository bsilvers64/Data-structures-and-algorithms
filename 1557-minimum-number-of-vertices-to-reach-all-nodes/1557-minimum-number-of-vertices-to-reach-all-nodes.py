class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        roots = []
        tracker = set()
        for _, j in edges:
            tracker.add(j)
        for i in range(n):
            if i not in tracker: roots.append(i)

        return roots