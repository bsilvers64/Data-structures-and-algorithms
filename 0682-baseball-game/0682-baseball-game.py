class Solution:
    def calPoints(self, ops: List[str]) -> int:
        st = collections.deque()

        for i in ops:
            print(st)
            if i == 'C':
                st.pop()
            elif i == 'D':
                st.append(st[-1]*2)
            elif i == '+':
                st.append(st[-1] + st[-2])
            else:
                st.append(int(i))
            
        return sum(st)
