class Solution:
    def trap(self, height: List[int]) -> int:

        N = len(height)
        left_max_wall, right_max_wall = [0] * N, [0]* N
        l_wall, r_wall = 0, 0

        for i in range(N):
            left_max_wall[i] = l_wall
            l_wall = max(l_wall, height[i])
        
        for i in range(N-1, -1, -1):
            right_max_wall[i] = r_wall
            r_wall = max(r_wall, height[i])
        
        water_collected = 0

        for i in range(N):
            potential_water = min(left_max_wall[i], right_max_wall[i]) - height[i]
            potential_water = potential_water if potential_water > 0 else 0
            water_collected += potential_water

        return water_collected

