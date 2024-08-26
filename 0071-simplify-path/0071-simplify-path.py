class Solution:
    def simplifyPath(self, path: str) -> str:
        curr = ''
        st = []
        N = len(path)
        i = 0
        while i < N:
            if path[i] == "/":
                i += 1
            else:
                while i < N and path[i] != "/":
                    curr += path[i]
                    i += 1
                if st and curr == "..":
                    st.pop()
                elif curr not in {".", ".."}:
                    st.append(curr)
                curr = ""

        ans = ""
        for i in st:
            ans += "/"
            ans += i
            
        return ans if ans else "/"
            