class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check(w):
            n = 0
            curr = 0
            i = 0
            while i < len(weights):
                while curr <= w and i < len(weights):
                    curr += weights[i]
                    i += 1
                n += 1
                if curr > w:
                    curr = 0
                    i -= 1
                if n > days: return False
            return True

        l, r = 1, sum(weights)

        result = -1
        while l <= r:
            mid = (l+r)//2
            if check(mid):
                r = mid - 1
                result = mid
            else:
                l = mid + 1

        return result