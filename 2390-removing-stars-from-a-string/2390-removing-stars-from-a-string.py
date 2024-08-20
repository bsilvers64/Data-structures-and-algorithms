class Solution:
    def removeStars(self, s: str) -> str:
        st = collections.deque()
        for i in s:
            if i == '*':
                st.pop()
            else:
                st.append(i)
        return "".join(map(str, st))