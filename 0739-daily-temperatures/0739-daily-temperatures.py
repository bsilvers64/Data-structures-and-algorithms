class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st, res = deque(), [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while st and st[-1][0] < temp:
                _, index = st.pop()
                res[index] = i-index
            st.append([temp, i])

        return res