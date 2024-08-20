class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i = 0
        st = []
        for n in pushed:
            st.append(n)

            while st and i < len(popped) and st[-1] == popped[i]:
                st.pop()
                i += 1
        
        return False if st else True