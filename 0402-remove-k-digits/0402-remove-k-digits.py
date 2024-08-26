class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st = []

        for i in num:
            if st:
                while st and k and st[-1] > i:
                    st.pop()
                    k -= 1
            st.append(i)

        st = st[:len(st)-k]

        res = ''.join(st).lstrip('0')
        return res if res else "0"