class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for i in asteroids:
            while st and st[-1] > 0 and i < 0:
                diff = st[-1] + i

                if diff == 0:
                    i = 0
                    st.pop()
                elif diff > 0: i = 0
                else:
                    st.pop()
            
            if i: st.append(i)

        return st