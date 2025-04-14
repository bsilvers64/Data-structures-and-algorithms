class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        N = len(piles)
        def check(k):
            hours = 0
            for bananas in piles:
                hours += ceil(bananas/k)
            return hours <= h

        l, r = 1, max(piles)

        k = r
        while l < r:
            mid = (l+r)//2
            if check(mid):
                k = mid
                r = mid 
            else:
                l = mid + 1

        return k