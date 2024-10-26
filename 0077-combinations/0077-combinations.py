class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        sub = []
        def bk(start):
            if len(sub) == k:
                res.append(sub[:])
                return
            for i in range(start, n+1):
                sub.append(i)
                bk(i+1)
                sub.pop()

        bk(1)
        return res