class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        paranthesis = []
        def recurse(op, cl):
            nonlocal paranthesis
            if not op and not cl:
                ans.append(''.join(paranthesis[:]))
            if op > 0:
                paranthesis.append('(')
                recurse(op-1, cl)
                paranthesis.pop()
            if cl > op:
                paranthesis.append(')')
                recurse(op, cl-1)
                paranthesis.pop()

        recurse(n, n)
        return ans