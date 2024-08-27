class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        st = []
        for i in s:
            if st and st[-1][0] == i:
                st.append([i, st[-1][1] + 1])
                if st[-1][1] == k:
                    j = 0
                    while (j < k): 
                        st.pop()
                        j += 1
            else:
                st.append([i, 1])
            #print(st)
        
        ans = ""
        for i in st:
            ans += i[0]
        return ans