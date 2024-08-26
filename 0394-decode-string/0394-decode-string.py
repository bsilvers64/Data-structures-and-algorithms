class Solution:
    def decodeString(self, s: str) -> str:
        st = []

        for i in s:
            if i != "]":
                st.append(i)
            else:
                curr, count = "", ""
                while st[-1] != "[":
                    curr = st.pop() + curr
                st.pop()
                while st and st[-1].isdigit():    
                    count = st.pop() + count
                st.append(int(count)*curr)
            print(st)
                
        return "".join(st)