class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for i in asteroids:
            while st and st[-1] > 0 and i < 0:
                diff = i + st[-1]

                if diff > 0:
                    i = 0
                elif diff == 0:
                    i = 0
                    st.pop()
                else:
                    st.pop()
            
            if i:
                st.append(i)

        return st