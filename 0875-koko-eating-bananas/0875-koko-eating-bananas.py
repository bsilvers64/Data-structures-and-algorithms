class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def k_works(k):
            hours = h
            for bananas in piles:
                hours -= ceil(bananas/k)
                if hours < 0: return False
            return hours >= 0

        min_k = 0
        l, r = 1, max(piles)    

        while l <= r:
            mid = (l + r) // 2
            if k_works(mid): 
                min_k = mid
                r = mid - 1
            else:
                l = mid + 1

        return min_k