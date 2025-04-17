class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height)
        water_collected = 0
        left_high, right_high = height[0], height[-1]
        leftmax, rightmax = [left_high] * N, [right_high] * N

        for i in range(1, N):
            leftmax[i] = left_high
            left_high = max(left_high, height[i])
            rightmax[N-i-1] = right_high
            right_high = max(right_high, height[N-i-1])
        
        for i in range(N):
            water_collected += max(0, min(leftmax[i], rightmax[i]) - height[i])

        return water_collected