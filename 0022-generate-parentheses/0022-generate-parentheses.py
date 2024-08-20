class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def adder(s, c, o):
            if not c and not o: 
                ans.append(s)
                return
            if c > o: 
                adder(s + ')', c - 1, o)
            if o > 0:
                adder(s + '(', c, o - 1)

        adder('(', n, n - 1)
        return ans