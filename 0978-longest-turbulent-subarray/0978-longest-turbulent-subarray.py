class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        high, low = 1, 1
        prev_high, prev_low = 1, 1
        ans = 1
        for i in range(1, n):
            if arr[i-1] < arr[i]:
                high = prev_low + 1
            elif arr[i-1] > arr[i]:
                low = prev_high + 1
            ans = max(ans, low, high)
            prev_high, prev_low = high, low
            high, low = 1, 1

        return ans