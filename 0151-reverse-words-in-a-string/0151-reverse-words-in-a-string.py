class Solution:
    def reverseWords(self, s: str) -> str:
        x = collections.deque()
        start = -1

        i = 0

        while i < len(s):
            if s[i] != " ":
                start = i

                while i < len(s) and s[i] != " ":
                    i += 1
                x.appendleft(s[start:i])
                x.appendleft(" ")
                
            i += 1

        return "".join(x)[1:]