class Solution:
    def removeKdigits(self, nums: str, k: int) -> str:
        st = []

        for num in nums:
            while st and k and st[-1] > num:
                st.pop()
                k -= 1
            st.append(num)
        
        st = st[:len(st)-k]

        res = "".join(st).lstrip("0")
        return res if res else "0"