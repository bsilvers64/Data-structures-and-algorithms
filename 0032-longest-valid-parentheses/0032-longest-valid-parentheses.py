class Solution:
    def longestValidParentheses(self, s: str) -> int:
        st = []
        N = len(s)
        longest = 0

        for i in range(N):
            if s[i] == "(": st.append(i)
            else:
                if st: 
                    if s[st[-1]] == "(": st.pop()
                    else:
                        st.append(i)
                else: 
                    st.append(i)
        
        if len(st) == 0: return N

        a = N

        while st:
            b = st.pop()
            longest = max(longest, a-b-1)
            a = b

        return max(longest, a)
        
        