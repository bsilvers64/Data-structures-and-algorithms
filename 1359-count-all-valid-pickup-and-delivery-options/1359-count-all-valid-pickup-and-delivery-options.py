class Solution:
    def countOrders(self, n: int) -> int:
        ans = 1
        slots = 2*n
        mod = 10**9 + 7

        while slots:
            ways = slots * (slots-1) // 2
            ans = (ans * ways) % mod
            slots -= 2

        return ans % mod