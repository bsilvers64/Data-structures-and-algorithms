class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        highs, lows = [1] * n, [1] * n
        ans = 1
        for i in range(1, n):
            if arr[i-1] < arr[i]:
                highs[i] = lows[i-1] + 1
            elif arr[i-1] > arr[i]:
                lows[i] = highs[i-1] + 1
            ans = max(ans, lows[i], highs[i])

        return ans