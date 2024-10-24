class Solution:
    def minCost(self, colors: str, nt: List[int]) -> int:
        l, r, N = 0, 1, len(nt)
        ans = 0
        while r < N:
            print(l, r)
            if colors[l] != colors[r]:
                l = r
            else:
                if nt[l] <= nt[r]:
                    ans += nt[l]
                    l = r
                else:
                    ans += nt[r]
            r += 1

        return ans