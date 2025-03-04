class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            while stack and stack[-1] > 0 and asteroid < 0:
                diff = stack[-1] - abs(asteroid)
                if diff > 0: asteroid = 0
                elif diff < 0: stack.pop()
                else:
                    stack.pop()
                    asteroid = 0

            if asteroid != 0: stack.append(asteroid) 


        return stack
