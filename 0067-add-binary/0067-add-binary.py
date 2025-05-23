class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = a[::-1], b[::-1]
        res = []
        carry = 0

        for i in range(max(len(a), len(b))):
            digit_a = int(a[i]) if i < len(a) else 0
            digit_b = int(b[i]) if i < len(b) else 0
            total = digit_a + digit_b + carry
            carry = total // 2
            total = total % 2
            res.append(str(total))
        
        if carry: res.append(str(carry))
        return "".join(reversed(res))