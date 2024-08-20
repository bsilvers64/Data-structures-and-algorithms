class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = collections.deque()
        ops = {'+', '/', '*', '-'}
        for i in tokens:
            if i not in ops:
                st.append(int(i))
            else:
                y = st.pop()
                x = st.pop()
                if i == '+': st.append(x+y)
                elif i == '*': st.append(x*y)
                elif i == '-': st.append(x-y)
                elif i == '/': st.append(int(x/y))
            #print(st, i)
            
           
        return int(st[0])                                
